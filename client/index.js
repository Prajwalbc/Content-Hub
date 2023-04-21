window.addEventListener("load", (event) => {
    console.log("Started");
  });

async function getData(url) {
    const response = await fetch(url);
    let data = await response.json();
    console.log(data.stud1);
}
getData("http://127.0.0.1:5000/");