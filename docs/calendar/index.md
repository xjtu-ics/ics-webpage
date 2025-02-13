---
hide:
  - toc
  - navigation
---
<!DOCTYPE html>
<html lang="en">

<head>
  <link href='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.8/index.global.min.css' rel='stylesheet' />
  <style>
    #calendar {
      width: 100%;
      height: 80vh;
      margin: 0 auto;
    }

    @media (max-width: 768px) {
      #calendar {
        width: 95%;
        height: 70vh;
      }

      .fc-header-toolbar {
        flex-direction: column;
        align-items: center;
      }

      .fc-button-group {
        margin-bottom: 5px;
      }
    }

    @media (min-width: 768px) and (max-width: 992px) {
      #calendar {
        width: 92%;
        height: 75vh;
      }
    }
  </style>
  <style>
    .event-content {
      border-radius: 8px;
      padding: 8px 12px;
      width: 240px;
      background: var(--md-default-bg-color);
      color: var(--md-default-fg-color);
      box-shadow: var(--md-shadow-z2);
      font-family: var(--md-text-font-family);
      line-height: 1.4;
      border: 1px solid var(--md-default-fg-color--lightest);
      transition: all 0.15s ease;
      overflow-wrap: break-word;
      word-break: break-all;
      white-space: normal;
    }

    .event-content h3 {
      margin: 0 0 2px 0;
      padding: 0;
      font-size: 1.1em;
      font-weight: 600;
      color: var(--md-primary-fg-color);
      border-left: 3px solid var(--md-accent-fg-color);
      padding-left: 8px;
    }

    .event-content p {
      margin: 1px 0;
      padding: 0 0 0 8px;
      font-size: 0.92em;
      color: var(--md-default-fg-color--light);
      line-height: 1.5;
      position: relative;
    }

    .event-content a {
      color: var(--md-accent-fg-color);
      text-decoration: none;
      font-weight: 500;
      transition: color 0.15s ease;
      display: inline-block;
      padding: 2px 4px;
      border-radius: 3px;
    }

    .event-content a:hover {
      color: var(--md-primary-fg-color);
      background-color: var(--md-accent-fg-color--transparent);
      text-decoration: underline;
    }

    .event-content p:not(:last-child)::after {
      content: "";
      display: block;
      height: 1px;
      background: var(--md-default-fg-color--lightest);
      margin: 2px 0;
      opacity: 0.3;
    }
  </style>
</head>

<body>
  <div id='calendar'></div>
  <script src='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.8/index.global.min.js'></script>
  <script>
    document.addEventListener('DOMContentLoaded', function () {
      fetch('../static/data/events.json')
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(eventsData => {
          var events = eventsData;
          var calendarEl = document.getElementById('calendar');
          var calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth',
            initialDate: '2025-02-17',
            headerToolbar: {
              left: 'prev,next today',
              center: 'title',
              right: 'dayGridMonth'
            },
            events: events,
            eventContent: function (arg) {
              var teacher = arg.event.extendedProps.teacher;
              var location = arg.event.extendedProps.location;
              var ppt = arg.event.extendedProps.pptLink;
              var theme = arg.event.extendedProps.theme;
              var eventContent = '<div class="event-content">';
              eventContent += '<h3>' + arg.event.title + '</h3>';
              eventContent += '<p>' + arg.event.start.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
              eventContent += '-' + arg.event.end.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) + '</p>';
              eventContent += '<p>' + teacher + '@' + location + '</p>';
              eventContent += '<p><a href="' + ppt + '" target="_blank">' + theme + '</a></p>';
              eventContent += '</div>';
              return { html: eventContent };
            }
          });
          calendar.render();
        })
        .catch(error => {
          console.error('Error loading the JSON file:', error);
        });
    });
  </script>
</body>

</html>