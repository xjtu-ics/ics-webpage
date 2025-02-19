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
  <script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js"></script>
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
          const { Instructors, location, pptLink, theme } = extendedProps;
          const teacherHtml = Instructors != "" ? `<p>${Instructors}@${location}</p>` : ``;
          const themeHtml = pptLink != "" ? `<p><a href="${pptLink}" target="_blank">${theme}</a></p>` : `<p>${theme}</p>`;
          const timeHtml = `<p>${start.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })} - 
                 ${end.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</p>`;
          const eventContent = `
            <div class="event-content">
              <h3>${title}</h3>
              ${timeHtml}
              ${teacherHtml}
              ${themeHtml}
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
      let allEvents = [];
      return fetch('../static/data/events.csv')
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.text();
        })
        .then(fileContent => {
          Papa.parse(fileContent, {
            header: true,
            step: function(res) {
              const Instructors = 'Instructors' in res.data
                                ? res.data.Instructors
                                : ``;
              const location = 'location' in res.data
                                ? res.data.location
                                : ``;
              const theme = 'theme' in res.data
                                ? res.data.theme
                                : ``;
              const pptLink = res.data.pptLink != ""
                                ? `../` + res.data.pptLink
                                : ``; 
              allEvents.push({
                title: res.data.title,
                start: res.data.start,
                end: res.data.end,
                extendedProps : {
                  Instructors: res.data.Instructors,
                  location: res.data.location,
                  theme: res.data.theme,
                  pptLink : pptLink
                }
              });
              console.log(res.data)
            }
          })
          return allEvents;
        })
        .catch(error => {
          console.error('Error fetching or parsing CSV:', error);
        })
        
    }
  </script>
</body>
</html>