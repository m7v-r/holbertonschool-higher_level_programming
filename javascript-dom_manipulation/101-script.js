document.addEventListener('DOMContentLoaded', () => {
  const btnTranslate = document.querySelector('#btn_translate');
  const langSelect = document.querySelector('#language_code');
  const helloDiv = document.querySelector('#hello');

  btnTranslate.addEventListener('click', () => {
    const lang = langSelect.value;
    if (lang) {
      const url = `https://hellosalut.stefanbohacek.com/?lang=${lang}`;
      fetch(url)
        .then((response) => response.json())
        .then((data) => {
          helloDiv.textContent = data.hello;
        });
    }
  });
});
