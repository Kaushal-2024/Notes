
# CSS Notes

## Flexbox

Flexbox is a layout model in CSS designed to provide a more efficient way to layout, align, and distribute space among items in a container, even when their size is unknown or dynamic.

### `row-wrapper`

This class represents a container with flexbox properties applied to create a horizontal layout with items evenly spaced along the main axis.

```css
.row-wrapper {
  display: flex; /* Use flexbox */
  align-items: center; /* Align items vertically */
  justify-content: space-between; /* Distribute space evenly between items */
}
```

### `column-wrapper`

This class represents a container with flexbox properties applied to create a vertical layout with items stacked on top of each other.

```css
.column-wrapper {
  display: flex; /* Use flexbox */
  flex-direction: column; /* Stack items vertically */
  align-items: center; /* Align items horizontally */
  justify-content: center; /* Align items vertically */
}
```

## Grid

Grid layout is a two-dimensional layout system for the web. It lets you lay out items into rows and columns with more control than flexbox.

```css
.grid {
  display: grid; /* Use grid layout */
  grid-template-columns: 1fr 500px 1fr; /* Define column sizes */
  grid-template-rows: 100px 200px; /* Define row sizes */
  place-items: center; /* Center items in the grid */
}
```

## Responsive Design

Responsive design ensures that your website looks good and functions well on all devices and screen sizes.

### Clamp Instead of Media Query

Using `clamp()` function for responsive design instead of traditional media queries.

### Aspect Ratio Property

Utilizing the `aspect-ratio` property to maintain the aspect ratio of elements.

### Column Count & Gap

Using `column-count` and `gap` properties for creating multi-column layouts with spacing between columns.

### Units

Using `ch` and `vw` units for sizing elements, providing relative sizing based on viewport width and character width.

## Dynamic Animations

Animating text dynamically on scrolling for a more engaging user experience.

```css
@keyframes scroll-reveal {
  to {
    background-size: 100% 100%;
  }
}

.scroll-reveal span {
  color: hsla(0, 0%, 100%, 0.2);
  background-clip: text;
  background-repeat: no-repeat;
  background-size: 0% 100%;
  background-image: linear-gradient(90deg, white, white);
  animation: scroll-reveal linear forwards;
}

.scroll-reveal h2 span {
  animation-range-start: cover 20vh;
  animation-range-end: cover 30vh;
}

.scroll-reveal p span {
  animation-range-start: cover 22.5vh;
  animation-range-end: cover 50vh;
}
```


.scroll-reveal span {
  color: hsla(0, 0%, 100%, 0.2);
  background-clip: text;
  background-repeat: no-repeat;
  background-size: 0% 100%;
  background-image: linear-gradient(90deg, white, white);
  animation: scroll-reveal linear forwards;
}

.scroll-reveal h2 span {
  animation-range-start: cover 20vh;
  animation-range-end: cover 30vh;
}

.scroll-reveal p span {
  animation-range-start: cover 22.5vh;
  animation-range-end: cover 50vh;
}