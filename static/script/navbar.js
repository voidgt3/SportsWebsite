// Selecting elements
const nav_toggle = document.querySelector('.nav_toggle');
const nav_toggle_icon = document.querySelector('.nav_toggle ion-icon');
const nav_menu = document.querySelector('.nav_menu');

// Adding click event listener to nav_toggle
nav_toggle.addEventListener('click', () => {
  // Toggle the 'active' class on nav_menu
  nav_menu.classList.toggle('active');

  // Toggle the icon name based on nav_menu's 'active' state
  nav_toggle_icon.setAttribute('name',
    nav_menu.classList.contains('active') ? 'close-outline' : 'menu-outline'
  );
});
