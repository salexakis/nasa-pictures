const dateform = document.getElementById('search-form');
const loading = document.getElementById('loading');
const container = document.getElementById('image-container');


//Add Event Listener for date selection form
dateform.addEventListener("submit", function(e){
  e.preventDefault();
  fetch_data();
  }
    
);


function showLoading(){
  loading.style.visibility = 'visible';
}


function hideLoading(){
  loading.style.visibility = 'hidden';
}


async function fetch_data(){

  showLoading();

  try {
    // Use of flask-cors allowing the fetch api call not being blocked even though the origin of the call is not the same (http://localhost:5000 and http://192.168.1.10:5000)
    let api_call = await fetch(`http://192.168.1.10:5000/data?start_date=${dateform['start_date'].value}&end_date=${dateform['end_date'].value}`);
    let response = await api_call.json();
    // console.log(response);
    
    hideLoading();

    if (response.code){
      alert(response.msg);
    } else {
      container.style.visibility = 'visible';
      container.innerHTML = '';
      let insertedElement = '';
      for (let i=0; i<response.length; i++){
        if (response[i].media_type === 'image') {
          insertedElement = `<a href="${response[i].hdurl}" target="_"><img src="${response[i].url}" alt="Picture"></img></a>`; 
        } else if (response[i].media_type === 'video') {
          insertedElement = `<a href="${response[i].url}" target="_"><iframe src="${response[i].url}" frameborder="0"></iframe></a>`; 
        }

        container.innerHTML += `
        <div class="image-item">
        <h3>"${response[i].title}"</h3>
        ${insertedElement}
        <p>${response[i].explanation}</p>
        <h4>Copyright: ${response[i].copyright}</h4>
        <h4>Date: ${response[i].date}</h4>
        </div>`;

      }

    }

  } catch (error) {
    console.log(error); 
  }
}
