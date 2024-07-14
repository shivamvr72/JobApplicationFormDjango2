try{
  addrow = document.querySelector("#add")
  addrow.addEventListener("click", createNewEduRow)

  remove = document.querySelector("#remove")
  remove.addEventListener("click", removeRow)


  divmain = document.querySelector("#education")

  idcount = 0

  function createNewEduRow(){
    idcount += 1
    divm = document.createElement("div")
    divm.setAttribute("class", "comform")
    
    id = document.createElement("input")
    id.setAttribute("hidden", true)
    id.setAttribute("name", "id")
    id.setAttribute("value", "newedu")

    authority = document.createElement("label")
    authority.innerHTML = "Education authority:"
    authority.setAttribute("for", `id_education_authority${idcount}`)
    authorityInput = document.createElement("input")
    authorityInput.setAttribute("name", "education_authority")
    authorityInput.setAttribute("id", `id_education_authority${idcount}`)
    authorityInput.setAttribute("placeholder", "education_authority")
    authorityInput.setAttribute("class", "education_authority")
    authorityInput.setAttribute("class", "form-control")


    course = document.createElement("label")
    course.innerHTML = "Course:"
    course.setAttribute("for", `id_course${idcount}`)
    courseInput = document.createElement("input")
    courseInput.setAttribute("id", `id_course${idcount}`)
    courseInput.setAttribute("name", "course")
    courseInput.setAttribute("placeholder", "course")
    courseInput.setAttribute("class", "form-control")

    passyear = document.createElement("lable")
    passyear.innerHTML = "Passing Year:"
    passyear.setAttribute("for", `id_passing_year${idcount}`)
    passyearInput = document.createElement("input")
    passyearInput.setAttribute("name", `passing_year`)
    passyearInput.setAttribute("id", `id_passing_year${idcount}`)
    passyearInput.setAttribute("placeholder", "passing_year")
    passyearInput.setAttribute("class", "form-control")

    percentage = document.createElement("lable")
    percentage.innerHTML = "Percentage: "
    percentage.setAttribute("for", `id_percentage${idcount}`)
    percentageInput = document.createElement("input")
    percentageInput.setAttribute("name", "percentage")
    percentageInput.setAttribute("id", `id_percentage${idcount}`)
    percentageInput.setAttribute("placeholder", "percentage")
    percentageInput.setAttribute("class", "form-control")

    divm.appendChild(id)
    divm.appendChild(authority)
    divm.appendChild(authorityInput)
    divm.appendChild(course)
    divm.appendChild(courseInput)
    divm.appendChild(passyear)
    divm.appendChild(passyearInput)
    divm.appendChild(percentage)
    divm.appendChild(percentageInput)

    divmain.appendChild(divm)
  }


  function removeRow(){
    divs = document.querySelectorAll(".comform")
    if(divs.length < 2){
      alert("atlest a row required!")
      return
    }
    divmain.removeChild(divmain.lastElementChild);
  }
}
catch{
  console.log("education not found");
}


// for the work exprience
try{
  divwork = document.querySelector("#workexp")

  addrow = document.querySelector("#addw")
  addrow.addEventListener("click", createNewWorkRow)

  remove = document.querySelector("#removew")
  remove.addEventListener("click", removeRowWork)

  wcount = 0
  function createNewWorkRow(){
    wcount += 1
    divm = document.createElement("div")
    divm.setAttribute("class", "comform")

    id = document.createElement("input")
    id.setAttribute("hidden", true)
    id.setAttribute("name", "id")
    id.setAttribute("value", "newwork")

    company = document.createElement("label")
    company.innerHTML = "Company:"
    company.setAttribute("for", `id_company${wcount}`)
    companyInput = document.createElement("input")
    companyInput.setAttribute("name", "company")
    companyInput.setAttribute("id", `id_company${wcount}`)
    companyInput.setAttribute("placeholder", "company")
    companyInput.setAttribute("class", "form-control")


    design = document.createElement("label")
    design.innerHTML = "Desingnation:"
    design.setAttribute("for", `id_desingnation${wcount}`)
    designInput = document.createElement("input")
    designInput.setAttribute("id", `id_desingnation${wcount}`)
    designInput.setAttribute("name", "desingnation")
    designInput.setAttribute("placeholder", "desingnation")
    designInput.setAttribute("class", "form-control")

    fromyear = document.createElement("lable")
    fromyear.innerHTML = "From year:"
    fromyear.setAttribute("for", `id_from_year${wcount}`)
    fromyearInput = document.createElement("input")
    fromyearInput.setAttribute("name", `from_year`)
    fromyearInput.setAttribute("id", `id_from_year${wcount}`)
    fromyearInput.setAttribute("placeholder", "from_year")
    fromyearInput.setAttribute("class", "form-control")

    toyear = document.createElement("lable")
    toyear.innerHTML = "To year: "
    toyear.setAttribute("for", `id_to_year${wcount}`)
    toyearInput = document.createElement("input")
    toyearInput.setAttribute("name", "to_year")
    toyearInput.setAttribute("id", `id_to_year${wcount}`)
    toyearInput.setAttribute("placeholder", "to_year")
    toyearInput.setAttribute("class", "form-control")

    divm.appendChild(id)
    divm.appendChild(company)
    divm.appendChild(companyInput)
    divm.appendChild(design)
    divm.appendChild(designInput)
    divm.appendChild(fromyear)
    divm.appendChild(fromyearInput)
    divm.appendChild(toyear)
    divm.appendChild(toyearInput)

    divwork.appendChild(divm)
  }


  function removeRowWork(){
    divs = document.querySelectorAll(".comform")
    if(divs.length < 2){
      alert("atlest a row required!")
      return
    }
    divwork.removeChild(divwork.lastElementChild);
  }
}catch{
  console.log("education not found");
}




// let prev = document.getElementById("prev")
// prev.addEventListener("click", fetchSessionDataS)

// function fetchSessionDataS(){
//   let value = sessionStorage.getItem('basic_details');
//   console.log(value);
// }