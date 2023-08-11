const student = {
    firstName: "nima",
    lastName: "gol",
    age: 20,
    skills: ["JS", "python"],
    country: "Iran",
    enrolled: true
  };
  
  localStorage.setItem("student", JSON.stringify(student));
  
  const retrievedStudent = JSON.parse(localStorage.getItem("student"));
  console.log(retrievedStudent);