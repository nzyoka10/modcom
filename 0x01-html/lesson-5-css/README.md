# CSS (Cascading Style Sheets)

CSS is a language used to describe the presentation of a document written in HTML or XML. It controls the layout, colors, fonts, and overall appearance of web pages.

## Key Concepts

### 1. CSS Syntax
A CSS rule consists of a selector and a declaration block.

```css
selector {
    property: value;
}
```

- **Selector**: Targets the HTML element(s) to style.
- **Declaration Block**: Contains one or more declarations.
  - **Property**: Specifies what to style (e.g., color, font-size).
  - **Value**: Specifies the value of the property.

### 2. Ways to Include CSS

1. **Inline CSS**
   - Applied directly to HTML elements using the `style` attribute.
   - **Example**:
     ```html
     <p style="color: blue; font-size: 20px;">This is a blue, large text.</p>
     ```

2. **Internal CSS**
   - Defined within a `<style>` tag in the `<head>` section of an HTML document.
   - **Example**:
     ```html
     <!DOCTYPE html>
     <html>
     <head>
         <style>
             p {
                 color: blue;
                 font-size: 20px;
             }
         </style>
     </head>
     <body>
         <p>This is a blue, large text.</p>
     </body>
     </html>
     ```

3. **External CSS**
   - Linked to an HTML document via a separate `.css` file.
   - **Example**:
     ```html
     <!DOCTYPE html>
     <html>
     <head>
         <link rel="stylesheet" type="text/css" href="styles.css">
     </head>
     <body>
         <p>This is a blue, large text.</p>
     </body>
     </html>
     ```
   - **External CSS file (styles.css)**:
     ```css
     p {
         color: blue;
         font-size: 20px;
     }
     ```

## CSS Selectors

### 1. Basic Selectors

- **Element Selector**: Targets elements by their tag name.
  ```css
  p {
      color: blue;
  }
  ```

- **Class Selector**: Targets elements with a specific class attribute (prefix with `.`).
  ```css
  .highlight {
      background-color: yellow;
  }
  ```

- **ID Selector**: Targets an element with a specific ID attribute (prefix with `#`).
  ```css
  #header {
      font-size: 24px;
  }
  ```

### 2. Group Selectors
Applies the same styles to multiple elements.
```css
h1, h2, h3 {
    color: green;
}
```

### 3. Combinators

- **Descendant Selector**: Targets elements that are descendants of a specified element.
  ```css
  div p {
      color: red;
  }
  ```

- **Child Selector**: Targets direct children of a specified element.
  ```css
  ul > li {
      list-style-type: none;
  }
  ```

- **Adjacent Sibling Selector**: Targets an element that immediately follows a specified element.
  ```css
  h1 + p {
      margin-top: 0;
  }
  ```

- **General Sibling Selector**: Targets elements that follow a specified element.
  ```css
  h1 ~ p {
      color: gray;
  }
  ```

## CSS Box Model

The CSS box model describes how elements are structured and rendered on a webpage.

### Components

1. **Content**
   - The actual content of the element, such as text or images.
   - **Example**:
     ```css
     .box {
         width: 200px;
         height: 100px;
     }
     ```

2. **Padding**
   - Space between the content and the border.
   - **Example**:
     ```css
     .box {
         padding: 20px;
     }
     ```

3. **Border**
   - Surrounds the padding and content.
   - **Example**:
     ```css
     .box {
         border: 2px solid black;
     }
     ```

4. **Margin**
   - Space outside the border, creating distance between elements.
   - **Example**:
     ```css
     .box {
         margin: 30px;
     }
     ```

### `box-sizing` Property

- **`content-box`** (default): Width and height apply only to the content area.
- **`border-box`**: Width and height include padding and border.

**Example**:
```css
.box {
    box-sizing: border-box;
    width: 200px;
    padding: 20px;
    border: 5px solid black;
}
```