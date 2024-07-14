document.querySelector('[for=id_gender_0]').hidden = true;



// // counters id, classes and events 
// const previous = document.getElementById("previous");
// const next = document.getElementById("next");
// const sbmit = document.getElementById("submit");
// previous.addEventListener("click", previosPage);
// next.addEventListener("click", nextPage);
// const components = document.getElementsByClassName("components");
// // dipslay counters id, classes and events 


// // making all fieldset invisible and submit button
// for(let component of components){
//     component.style.display = "none";
// }


// function basicField(){
//   console.log("basicField")
//   return true
// }

// function education(){
//   console.log("education")
//   return true
// }
// function workExperice(){
//   console.log("workExperice")
//   return true
// }
// function references(){
//   console.log("references")
//   return true
// }
// function preferences(){
//   console.log("preferences")
//   return true
// }
// function basicField(){
//   console.log("basicField")
//   return true
// }


// // moving the next page and checking validations
// function nextPage(){
    
//     const searchParams = window.location.search;
//     const urlParams = new URLSearchParams(searchParams);
//     const ids = urlParams.get("id");
    
//     // console.log("hello next")
    
//     // for basic form validation
//     if(displayCounter == 0){
//         if(basicField()){
//             console.log("BASIC OK", displayCounter);
//         } else{
//             return;
//         }
//     }
    
//     if(displayCounter == 1){
//         if(education()){
//             console.log("EDUCATION OK", displayCounter);
//         } else {
//             return;
//         }
//     }

//     if(displayCounter == 4){
//         if(workExperice()){
//             console.log("WORK OK", displayCounter);
//         } else {
//             return;
//         }
//     }
    

//     if(displayCounter == 5){
//         if(references()){
//             console.log("REF OK", displayCounter);
//         } else {
//             return;
//         }
//     }

    
//     if(displayCounter == 6){
//         if(preferences()){
//             console.log("PREF OK", displayCounter);
//         } else {
//             return;
//         }

//         if(ids){
//             next.innerHTML = "Update";
//         } else {
//             next.innerHTML = "Submit";
//         }
//     }      
    
//     displayCounter++;


//     if(displayCounter == 7){
//         if(ids){
//             // postDataUpdate()
//             alert("your data has been updated");   
//             // window.location.replace("http://localhost:8080/wireframeajax");
//         } else {
//             // postData();
//             alert("your response has been submited");
//             // window.location.replace("http://localhost:8080/wireframeajax");
//         }
        
//         displayCounter--;
//     }
  
//     previous.style.display = "block";
//     displayElement(displayCounter);

// }

// function previosPage(){
//     console.log(displayCounter)
//     if(displayCounter < 1){
//         previous.style.display = "none";
//         return;
//     } else {
//         // next.style.display = "block";
//         next.innerHTML = "next";
//         displayCounter--;
//         displayElement(displayCounter);
//     }
// }

// let displayCounter = 0;
// previous.style.display = "none";


// if(displayCounter == 0){
//     document.getElementById("0").style.display = "block";
//     console.log("sss");
// } else {
//     // document.getElementById("0").style.display = "none";
// }

// function displayElement(displayId){
//     for(let component of components){
//         component.style.display = "none";
//     }

//     if(displayCounter == displayId){
//         document.getElementById(String(displayId)).style.display = "block"; 
//     } else {
//         document.getElementById(String(displayId)).style.display = "none";
//     }
// }
