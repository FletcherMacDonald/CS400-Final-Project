// Function to display the corresponding tab content
function showTab(tabId) {
    // Hide all tabs
    const contents = document.querySelectorAll('.tab-content');
    contents.forEach(content => {
      content.classList.remove('active');
    });
  
    // Remove active class from all buttons
    const buttons = document.querySelectorAll('.tab-button');
    buttons.forEach(button => {
      button.classList.remove('active');
    });
  
    // Show the clicked tab content
    const activeContent = document.getElementById(tabId);
    activeContent.classList.add('active');
  
    // Add active class to the clicked button
    const activeButton = document.querySelector(`button[onclick="showTab('${tabId}')"]`);
    activeButton.classList.add('active');
  }
  
  // Initialize the first tab to be visible by default
  document.addEventListener("DOMContentLoaded", function() {
    showTab('about');
  });
  