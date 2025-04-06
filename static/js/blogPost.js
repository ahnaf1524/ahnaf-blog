document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("pre").forEach((pre) => {
    const code = pre.querySelector("code");
    if (!code) return;

    // Create copy button
    const button = document.createElement("button");
    button.className = "copy-btn";
    button.innerHTML = "📋 Copy";

    // Append button to <pre>
    pre.appendChild(button);

    // Add click event to copy code
    button.addEventListener("click", () => {
      navigator.clipboard.writeText(code.innerText).then(() => {
        button.innerHTML = "✅ Copied!";
        setTimeout(() => (button.innerHTML = "📋 Copy"), 1500);
      });
    });
  });
});
