### Conceptual Exercise

Answer the following questions below:

- What is React? When and why would you use it?
React is a front-end framework that helps us organize our JS, HTML and CSS into modular components. In regular JS, the high-level design pattern is to separate JS, CSS and HTML into separate files. React allows us to create components that include all JS/CSS/HTML for the component to work. 

We would use it if we were building a large web app and wanted our code organized this way to promote re-use and speed-up development. It is also easier to understand your components when they are organized this way as opposed to having their logic, html and css scattered across many files. 

- What is Babel?

Babel is an open-course JS transcompiler used to convert ES6+ (2015) into backwards compatible JS that can be run by older browsers. Additionally, Babel can transcompile JSX into JS. 

- What is JSX?

JSX is an extension of the JS language. JSX provides a way to structure component rendering using syntax familiar to many developers because it is similar to HTML. In React, we write our components in JSX.

const App = () => {
   return (
     <div>
       <p>Header</p>
       <p>Content</p>
       <p>Footer</p>
     </div>
   ); 
}

In the above example, there is an App component rendering a div that contains 3 paragraphs. This "HTML-like" JSX will be transcompiled into the correct JS needed to make those HTML elements. 

- How is a Component created in React?
  
  A component is created when the function that defines a given component is invoked. <UsernameForm /> would invoke UsernameForm, thus rendering UsernameForm. The component is written in JSX (described above), that JSX is transcompiled into the JS needed to create that particular component. 

  If any state associated with that component changes, that component will be re-rendered. 

- What are some difference between state and props?

  State is mutable, meaning it can change. Assigning new value to state is how React knows to re-render a component. State data is specific to a given component, but the state value and functions used to alter state value can be passed to other components. 

  props are immutable, meaning they cannot be changed. Props are passed into a component during rendering or there can be a default value if nothing is passed in. While props are immutable, we can have dynamic prop values that are created when parent passes state down as props. 

  If the state value changes the parent component will be re-rendered, passing a new prop value to the child. 

- What does "downward data flow" refer to in React?

  Downward Data Flows refers to uni-directional information flow within React. If state changes within a component, that change can only affect the component itself or any children that are receiving that state as a prop. The change cannot flow "up" to the parent of the component or "horizonally" to another unrelated component that isn't a child of the affected component. 

  Downward Data Flow makes our React apps less error prone and easier to debug because we can tell what data is coming from where. 

- What is a controlled component?

  A controlled component is any component that can be completely controlled by React, its value as well as behavior. The state of the input is determined by Reacts own state. 
  
  In a controlled input, typing will no have no effect because the value of the form is determined by a state in React. Only by creating some sort of onChange function that updates the state based on user input can will we see any characters appearing in the input. 

  Because the current value of the input is known to React via a state, we can run logic based on whatever is in the input without having to submit the form. For example, we can mandate that a text field but have between 1 and 15 characters and display a warning to the user below the input if they are outside this range. 

- What is an uncontrolled component?

  An uncontrolled component is any component whose state is NOT controlled by React. This is a rare occurance but there are times when we need them. If dealing with a legacy codebase that doesn't use React it may be more hassle than its worth to try to integrate React with all the inputs. Additionally, file inputs have to be uncontrolled because the value is a file coming from the user, wouldn't make any sense for React to determine that value. 

- What is the purpose of the `key` prop when rendering a list of components?

  In React, each child in a list needs to have a unique, stable (not changing) key. The key allows React to determine which items have been added or removed from a list. We want them to be unique so that each key only applies to a single element, if elements share keys that defeats the purpose. Stable means that the key for a given element will have the same value each time it is rendered, we usually achieve this by having the key be an id from a table. 

- Why is using an array index a poor choice for a `key` prop when rendering a list of components?

  Using an array index is a poor choice for a key prop because the index values aren't guaranteed to be stable. If we add, remove, filter, sort elements then the index values will be altered, which in turn changes the key values. If we instead base the key on the id associated with the element from a table then the key is guaranteed to be stable. 

- Describe useEffect.  What use cases is it used for in React components?
  useEffect allows you to run code after a component has rendered. The default behavior is that it also runs after all re-renders but this behavior can be altered.  

  Common use cases are:
  1) When fetching data via an async function useEffect allows us to render the components before async functions return their response values.

  2) When setting a timer useEffect allows us to have a single timer that is re-created with a different starting value on each render instead of starting an additional timer on each render.  


- What does useRef do?  Does a change to a ref value cause a rerender of a component?

  useRef returns a mutable object with a key current, whose value is equal to the initial value passed into the hook. This object persists across renders (like state), mutating the object does not trigger a re-render. The returned object acts as a global variable even though it is scopped locally, this is useful if we need to access a variable like a timer id from outside the function that created the timer. Alternative would be using an actual global variable, which we want to avoid. 



- When would you use a ref? When wouldn't you use one?

  You would use refs if you want to be able to access the value created by useRef independent of scope. For example, if you have a timer function you can set 
  const timerId = useRef();
  and then
  timerId.current = setInterval(async () => {
  timerIf.current is now the timerId, but can be accessed outside the scope the timer function was declared in. 

  Another common use case would be slecting underlying DOM elements that we want to be able to access outside of the return block of our component. 

- What is a custom hook in React? When would you want to write one?

Custom hooks allow us to share logic between React components. 

We would want to write them if we have logic that will be used in more than 1 component or even if the logic will only be used in 1 component but we want to dry-up the code we could move modular chunks of it into custom hooks. 

An example would be a custom hook that toggles between true/false, which is a common state pattern in react. If we have multiple components that could use such a piece of state (even if they are using for different purposes) then we can create a useToggleState custom hook and import it into all components that need. 

An additional advantage is that if we want to change the toggle behavior we only need to change it in one place instead of changing it in many different components. 
