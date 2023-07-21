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
        <button id="book" class="book-button button button-secondary">Book</button>
      `,
  },
};

const calendar = new VanillaCalendar("#calendar", options);
calendar.init();

const nine = document.getElementById("morning");
const one = document.getElementById("afternoon");
const bookButton = document.getElementById("book");
let selectedTime;

nine.addEventListener("click", function (e) {
  selectedTime = nine.textContent;
  nine.classList.toggle("active");
  one.classList.remove("active");
});
one.addEventListener("click", function (e) {
  selectedTime = one.textContent;
  one.classList.toggle("active");
  nine.classList.remove("active");
});

bookButton.addEventListener("click", function () {
  fetch("/book", {
    method: "POST",
    body: JSON.stringify({
      date: _date,
      time: selectedTime,
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  }).then((response) => response.json());
});
