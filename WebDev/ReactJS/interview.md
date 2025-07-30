intro

Good morning, my name is Kaushal Tarapra. I’m a software developer with around 1 year of experience, currently working at EspakrBiz. During this time, I’ve worked primarily with React and TypeScript, building scalable and responsive web applications.

One of the key projects I contributed to was the Versio project, where I worked on component development, API integration, and state management.

I’m passionate about clean code, UI performance, and learning modern frontend technologies. I’m excited for the opportunity to contribute and grow further with your team.


*Batching in react
Batching is the process where React groups multiple state updates together into a single re-render to improve performance.

---

### 🔹 1. **React Hooks**

| Hook          | Purpose                                                   |
| ------------- | --------------------------------------------------------- |
| `useState`    | Manage local component state.                             |
| `useEffect`   | Handle side effects (API calls, subscriptions, timers).   |
| `useContext`  | Access shared data without prop drilling.                 |
| `useReducer`  | Manage complex state using reducers (like Redux pattern). |
| `useMemo`     | Memoize expensive calculations.                           |
| `useCallback` | Memoize functions to prevent re-renders.                  |
| `useRef`      | Access DOM or persist values across renders.              |

---

### 🔹 2. **Higher-Order Components (HOC)**

* **What**: Function that takes a component and returns an enhanced component.
* **Why**: Logic reuse (e.g., auth checks, theming).
* **When**: Wrap components to share behavior.
* **How**:

  ```js
  const withLogger = (Component) => (props) => {
    console.log('Render:', Component.name);
    return <Component {...props} />;
  };
  ```

---

### 🔹 3. **Lifecycle Methods (Class Components)**

| Phase      | Methods                                       |
| ---------- | --------------------------------------------- |
| Mounting   | `constructor`, `componentDidMount`            |
| Updating   | `shouldComponentUpdate`, `componentDidUpdate` |
| Unmounting | `componentWillUnmount`                        |

---

### 🔹 4. **State Management Basics**

* **State**: Internal data (via `useState`, `this.state`).
* **Props**: Data passed from parent.
* **Prop Drilling**: Passing props through multiple layers.
* **Context API**: Avoids prop drilling by sharing data globally.

---

### 🔹 5. **Redux / Zustand (Global State)**

* **Redux**:

  * Centralized state, strict structure (actions, reducers).
  * Use Redux Toolkit (RTK) for simplicity.
* **Zustand**:

  * Lightweight, simpler syntax, less boilerplate.
* **When to use**:

  * App-wide state, multiple consumers, or complex state interactions.

---

### 🔹 6. **Custom Hooks**

* **Why**: Reuse logic (e.g., fetch, localStorage).
* **How**:

  ```js
  function useLocalStorage(key, init) {
    const [value, setValue] = useState(() => JSON.parse(localStorage.getItem(key)) || init);
    useEffect(() => localStorage.setItem(key, JSON.stringify(value)), [value]);
    return [value, setValue];
  }
  ```

---

### 🔹 7. **Lazy Loading + Code Splitting**

* **Code Splitting**: Load only what’s needed.
* **Chunking**: Split large files into smaller ones.
* **Suspense**: Shows fallback while loading.

  ```js
  const LazyComp = React.lazy(() => import('./Comp'));
  ```

---

### 🔹 8. **Virtual DOM and Rendering**

| Concept           | Purpose                                                 |
| ----------------- | ------------------------------------------------------- |
| Virtual DOM       | Lightweight copy of the real DOM for efficient updates. |
| Reconciliation    | Compare old vs new Virtual DOM.                         |
| Diffing Algorithm | Finds minimal changes.                                  |
| React Fiber       | Incremental rendering engine for responsiveness.        |

---

### 🔹 9. **SSR vs CSR**

| Feature | SSR (Server-Side Rendering) | CSR (Client-Side Rendering) |
| ------- | --------------------------- | --------------------------- |
| Render  | On the server               | In the browser              |
| SEO     | Better SEO                  | Needs extra setup for SEO   |
| Speed   | Faster first paint          | Slower initial load         |

---

### 🔹 10. **Routing (with RBAC)**

* **react-router**: Navigation and routing.
* **Protected Routes**: Check auth before rendering route.
* **Query Params**: `useSearchParams`, `useLocation`.
* **Dynamic Routes**: Based on data (e.g., `/product/:id`).

---

### 🔹 11. **Testing**

| Type                                               | Tool/Use                     |
| -------------------------------------------------- | ---------------------------- |
| Unit Test                                          | Test component logic         |
| Integration                                        | Test flow between components |
| RTL (React Testing Library)\*\*: Tests UI behavior |                              |
| Best Practice                                      | Write testable, modular code |

---

### 🔹 12. **Async Handling**

* **API calls**: Done in `useEffect`.
* **Events**: Clicks, input handlers.
* **Promises**: Handle async logic cleanly.
* **Timers**: `setTimeout`, `setInterval` in `useEffect`.

---

### 🔹 13. **Code Quality Principles**

* **Reusability**: DRY (Don’t Repeat Yourself).
* **Readability**: Clear, consistent naming.
* **Modularity**: Small, single-purpose components.
* **Testability**: Write logic that’s easy to test.

---

### 🔹 14. **Performance Optimization**

| Technique               | Example                                |
| ----------------------- | -------------------------------------- |
| Lazy Loading            | Load pages/components as needed        |
| Memoization             | `React.memo`, `useMemo`, `useCallback` |
| Bundle Optimization     | Tree shaking, chunk splitting          |
| CDN/Server Optimization | Host assets via CDN                    |
| UX                      | Skeletons, shimmer UI                  |

---

### 🔹 15. **Styling Options**

| Approach          | Pros                            | Cons                            |
| ----------------- | ------------------------------- | ------------------------------- |
| Tailwind CSS      | Utility-first, fast             | Steeper learning curve          |
| CSS / SCSS        | Native, scoped with modules     | Can get messy in large projects |
| Styled-Components | JS-based, scoped styles         | Slight runtime overhead         |
| Bootstrap / MUI   | Prebuilt, responsive components | Less customizable               |
| StyleX            | Meta’s modern styling framework | Newer, still evolving           |

---

Would you like a downloadable PDF version for revision or interview prep?

