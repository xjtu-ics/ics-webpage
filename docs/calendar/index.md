---
hide:
  - toc
  - navigation
---
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Calendar</title>
  <link href="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.8/index.global.min.css" rel="stylesheet" />
  <link rel="stylesheet" href="../stylesheets/calendar.css">
  
</head>
<body>
  <div id="calendar"></div>
  <script src="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.8/index.global.min.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function () {
      // 初始化日历
      const calendarEl = document.getElementById('calendar');
      const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        initialDate: '2025-02-17',
        headerToolbar: {
          left: 'prev,next today',
          center: 'title',
          right: 'dayGridMonth'
        },
        events: [], // 初始时为空，后续通过 fetch 加载
        eventContent: function (arg) {
          const { title, start, end, extendedProps } = arg.event;
          const { teacher, location, pptLink, theme } = extendedProps;
          const eventContent = `
            <div class="event-content">
              <h3>${title}</h3>
              <p>${start.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })} - 
                 ${end.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</p>
              <p>${teacher}@${location}</p>
              <p><a href="${pptLink}" target="_blank">${theme}</a></p>
            </div>
          `;
          return { html: eventContent };
        }
      });
      calendar.render();

      fetchEvents().then(events => {
        calendar.addEventSource(events);
      }).catch(error => {
        console.error('Error loading the JSON file:', error);
        alert("Failed to load events. Please check your network connection or contact the administrator.");
      });
    });

    function fetchEvents() {
      return fetch('../static/data/events.json')
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        });
    }
  </script>
</body>
</html>