console.log('The JS file was found!');

const colors = [
  'red',
  'green',
  'blue',
  'pink',
  'purple',
  'yellow',
  'gray',
]

const ballElement = document.querySelector('#ball');
ballElement.addEventListener('mousemove', function() {
  ballElement.style.backgroundColor =
      colors[Math.floor(Math.random() * colors.length)];
});
