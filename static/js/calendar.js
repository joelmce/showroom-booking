let _date;
let time;

const options = {
  actions: {
    clickDay(e, dates) {
      _date = dates;
    },
  },
  DOMTemplates: {
    default: `
        <div class="vanilla-calendar-header">
          <div class="vanilla-calendar-header__content">
            <#Year /> | <#Month />
          </div>
          <#ArrowPrev />
          <#ArrowNext />
        </div>
        <div class="vanilla-calendar-wrapper">
          <div class="vanilla-calendar-content">
            <#Week />
            <#Days />
          </div>
        </div>
        <div class="times-container">
            <a class="time" id="morning">9:30am</a>
            <a class="time" id="afternoon">1:30pm</a>
        </div>
      `,
  },
};

const nine = document.getElementById("morning");
const one = document.getElementById("afternoon");
const bookButton = document.getElementById("book");

bookButton.addEventListener("click", function () {
  fetch("/book", {
    method: "POST",
    body: JSON.stringify({
      date: _date,
      time: "9:30am",
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  }).then((response) => response.json());
});

const calendar = new VanillaCalendar("#calendar", options);
calendar.init();
