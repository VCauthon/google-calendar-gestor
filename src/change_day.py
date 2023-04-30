import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Autenticación de credenciales
creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar'])

# Creación de servicio de la API de Google Calendar
service = build('calendar', 'v3', credentials=creds)

# Definición del tag de búsqueda
tag = 'mi_tag'

# Obtener todos los eventos que contienen el tag en su nombre
events_result = service.events().list(calendarId='primary', q=tag).execute()
events = events_result.get('items', [])

# Definir la nueva fecha de inicio y fin de los eventos (5 días después)
delta = datetime.timedelta(days=5)
new_start = (datetime.datetime.utcnow() + delta).isoformat() + 'Z'
new_end = (datetime.datetime.utcnow() + delta + datetime.timedelta(hours=1)).isoformat() + 'Z'

# Actualizar la fecha de inicio y fin de los eventos encontrados
if not events:
    print('No se encontraron eventos con el tag "{}".'.format(tag))
else:
    for event in events:
        event_id = event['id']
        event_start = event['start'].get('dateTime', event['start'].get('date'))
        event_end = event['end'].get('dateTime', event['end'].get('date'))
        event_summary = event['summary']

        # Aplicar cambio de fecha solo si el evento no es todo el día
        if 'T' in event_start and 'T' in event_end:
            event['start']['dateTime'] = new_start
            event['end']['dateTime'] = new_end
            updated_event = service.events().update(calendarId='primary', eventId=event_id, body=event).execute()
            print('Se ha actualizado el evento "{}" (ID: {})'.format(updated_event['summary'], updated_event['id']))
        else:
            print('El evento "{}" (ID: {}) es todo el día y no se puede modificar la hora.'.format(event_summary, event_id))

