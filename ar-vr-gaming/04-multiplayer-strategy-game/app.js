// Multiplayer Strategy Game — Interactive HTML5 Canvas Engine
const canvas = document.getElementById("stage");
const ctx = canvas.getContext("2d");
let score = 0;
let running = true;
const player = { x: 80, y: 180, r: 16, vy: 0 };
const orbs = Array.from({ length: 6 }, (_, i) => ({
  x: 240 + i * 110,
  y: 60 + Math.random() * 240,
  r: 12,
  speed: 2.2 + Math.random() * 1.6,
}));

canvas.addEventListener("mousemove", (e) => {
  const rect = canvas.getBoundingClientRect();
  player.y = Math.max(20, Math.min(canvas.height - 20, e.clientY - rect.top));
});

function loop() {
  ctx.fillStyle = "#0b0f19";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Subtle 3D perspective grid
  ctx.strokeStyle = "rgba(249, 115, 22, 0.14)";
  for (let x = 0; x < canvas.width; x += 40) {
    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
  }

  // Draw player
  ctx.fillStyle = "#f97316";
  ctx.beginPath();
  ctx.arc(player.x, player.y, player.r, 0, Math.PI * 2);
  ctx.fill();

  // Move & draw interactive targets
  for (const orb of orbs) {
    orb.x -= orb.speed;
    if (orb.x < -20) {
      orb.x = canvas.width + 30;
      orb.y = 30 + Math.random() * (canvas.height - 60);
    }
    const dist = Math.hypot(player.x - orb.x, player.y - orb.y);
    if (dist < player.r + orb.r) {
      score += 10;
      document.getElementById("score").textContent = String(score);
      orb.x = canvas.width + 40;
      orb.y = 30 + Math.random() * (canvas.height - 60);
    }
    ctx.fillStyle = "#38bdf8";
    ctx.beginPath();
    ctx.arc(orb.x, orb.y, orb.r, 0, Math.PI * 2);
    ctx.fill();
  }
  if (running) requestAnimationFrame(loop);
}
loop();
