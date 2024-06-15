// script for showing dropdown box for learning
function learningDropdown() {
  document.querySelector(".learning-dropdown-hidden-box").classList.toggle("learning-dropdown-box");
  document.querySelector(".learning-menu-heading-inactive").classList.toggle("learning-menu-heading-active");
  document.querySelector(".drp-down-btn1").classList.toggle("drp-down-btn-flipped");
  if (document.querySelector(".challenge-dropdown-box")) {
    challengeDropdown()
    
  }
  if (document.querySelector(".opportunities-dropdown-box")) {
    opportunitiesDropdown()
  }
  if (document.querySelector('.user-dropdown')) {
    userDropdown()
  }
}


// script for showing dropdown box for challenge

function challengeDropdown() {
  document.querySelector(".challenge-dropdown-hidden-box").classList.toggle("challenge-dropdown-box");
  document.querySelector(".challenge-menu-heading-inactive").classList.toggle("challenge-menu-heading-active");
  document.querySelector(".drp-down-btn2").classList.toggle("drp-down-btn-flipped");
  if (document.querySelector(".learning-dropdown-box")) {
    learningDropdown()
  }
  if (document.querySelector(".opportunities-dropdown-box")) {
    opportunitiesDropdown()
  }
  if (document.querySelector('.user-dropdown')) {
    userDropdown()
  }
}


// script for showing dropdown box for oppurtunity

function opportunitiesDropdown() {
  document.querySelector(".opportunities-dropdown-hidden-box").classList.toggle("opportunities-dropdown-box");
  document.querySelector(".opportunities-menu-heading-inactive").classList.toggle("opportunities-menu-heading-active");
  document.querySelector(".drp-down-btn3").classList.toggle("drp-down-btn-flipped");
  if (document.querySelector(".learning-dropdown-box")) {
    learningDropdown()
  }
  if (document.querySelector(".challenge-dropdown-box")) {
    challengeDropdown()
  }
  if (document.querySelector('.user-dropdown')) {
    userDropdown()
  }
}



// script for showing dropdown box for userdropdown in profile

function userDropdown() {
  document.querySelector(".user-dropdown-hidden").classList.toggle('user-dropdown');
  if (document.querySelector(".learning-dropdown-box")) {
    learningDropdown()
  }
  if (document.querySelector(".challenge-dropdown-box")) {
    challengeDropdown()
  }
  if (document.querySelector(".opportunities-dropdown-box")) {
    opportunitiesDropdown()
  }
}



// script for showing dropdown box for modes/stages and all

function toggleDropdown(dropdownId) {
  var dropdown = document.getElementById(dropdownId);
  dropdown.classList.toggle("show");
  var nestedDropdownId = dropdownId + "Nested";
  var nestedDropdown = document.getElementById(nestedDropdownId);
  if (nestedDropdown) {
    nestedDropdown.classList.remove("show"); 
  }
}


// function for getting search

function filterFunction() {
  const input = document.getElementById("myInput");
  const filter = input.value.toUpperCase();
  const div = document.getElementById("offlineDropdown"); 
  const options = div.getElementsByTagName("div");
  for (let i = 0; i < options.length; i++) {
    txtValue = options[i].textContent || options[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      options[i].style.display = "";
    } else {
      options[i].style.display = "none";
    }
  }
}



function selectOfflineOption(option) {
  console.log("Selected offline option:", option);
}

function selectMode(mode) {
  console.log("Selected mode:", mode);
}


//function to closse dropdown clicking whereever we clicks on the screen
window.onclick = function(event) {
  var locationDropdown = document.getElementById("offlineDropdown");
  if (!event.target.closest('.explore-filter-box')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (var i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }

    // Close the location dropdown
    if (locationDropdown.classList.contains('show')) {
      locationDropdown.classList.remove('show');
    }
  }
}




