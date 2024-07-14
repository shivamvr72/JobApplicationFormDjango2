error_msg = document.querySelectorAll(".errorlist")

error_msg.forEach((err, i) => {
  console.log(err)
});


try{
  document.querySelector('[for=id_gender_0]').hidden = true;
} catch {
  console.log();
}



try{
  document.querySelector('[for=id_techonologies-0-status_0]').hidden = true
  document.querySelector('[for=id_techonologies-1-status_0]').hidden = true
  document.querySelector('[for=id_techonologies-2-status_0]').hidden = true

} catch {
  console.log();
}
