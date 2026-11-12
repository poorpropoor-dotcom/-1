"""Flask server for the portfolio and public games page."""

import os
import time

from flask import Flask, jsonify, redirect, render_template_string, send_file, send_from_directory, url_for

app = Flask(__name__)

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_FILE = os.path.join(PROJECT_DIR, "frontend", "portfolio-winter2.html")
GAME_DIR = os.path.join(PROJECT_DIR, "frontend", "game")


@app.get("/")
def index():
    return redirect(url_for("portfolio_winter2"), code=302)


@app.get("/portfolio-winter2")
def portfolio_winter2():
    response = send_file(HTML_FILE, mimetype="text/html")
    response.headers["Cache-Control"] = "no-store"
    return response


@app.get("/game/")
def game_portal():
    games = []
    for root, _, filenames in os.walk(GAME_DIR):
        for filename in filenames:
            if filename.lower().endswith(".html"):
                games.append(os.path.relpath(os.path.join(root, filename), GAME_DIR))
    games.sort(key=str.casefold)
    return render_template_string(
        """<!DOCTYPE html>
<html lang="kaa">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#020a14">
  <title>Sinaw bólimi — Oyınlar</title>
  <style>
    * { box-sizing: border-box }
    body { min-height: 100vh; margin: 0; display: grid; place-items: center; padding: 2rem; color: #ddeeff; background: radial-gradient(ellipse at 50% 0, #0b2540 0, #020a14 60%); font-family: "Segoe UI", sans-serif; -webkit-user-select: none; user-select: none; cursor: none }
    main { width: min(720px, 100%); padding: clamp(1.5rem, 5vw, 3rem); background: rgba(10, 24, 40, .88); border: 1px solid #16334c; box-shadow: 0 24px 80px #0008 }
    .eyebrow { color: #00cfff; font: 600 .72rem Consolas, monospace; letter-spacing: .18em }
    h1 { margin: .8rem 0; font-size: clamp(2rem, 7vw, 3rem) }
    p { color: #89a9c5; line-height: 1.7 }
    .games { display: grid; gap: .8rem; margin: 2rem 0 }
    .game { display: flex; align-items: center; justify-content: space-between; gap: 1rem; padding: 1rem 1.2rem; color: #ddeeff; background: #071321; border: 1px solid #17334c; text-decoration: none; transition: .2s }
    .game:hover { border-color: #00cfff; transform: translateY(-2px); box-shadow: 0 0 24px #00cfff22 }
    .empty { padding: 1.2rem; border: 1px dashed #24445e; color: #89a9c5 }
    .back { display: inline-block; margin-top: .5rem; color: #00cfff; text-decoration: none }
    .back:hover { color: #fff }
    #game-cursor, #game-cursor-ring { position: fixed; top: 0; left: 0; z-index: 10; pointer-events: none; border-radius: 50%; transform: translate(-50%, -50%) }
    #game-cursor { width: 10px; height: 10px; background: #00cfff; mix-blend-mode: screen; transition: width .2s, height .2s }
    #game-cursor-ring { width: 34px; height: 34px; border: 1px solid rgba(0, 207, 255, .4); transition: left .08s linear, top .08s linear, width .25s, height .25s, border-color .25s }
    body.game-cursor-hover #game-cursor { width: 18px; height: 18px }
    body.game-cursor-hover #game-cursor-ring { width: 50px; height: 50px; border-color: rgba(0, 207, 255, .8) }
    @media (hover: none), (pointer: coarse) { body { cursor: auto } #game-cursor, #game-cursor-ring { display: none } }
  </style>
</head>
<body>
  <main>
    <div class="eyebrow">// OYINLAR HÁM JOYBARLAR</div>
    <h1>Sinaw bólimi <span aria-hidden="true">🎮</span></h1>
    <p>Bul jerde ózińiz islegen oyınlar hám basqa joybarlardı sınap kóriń.</p>
    <div class="games">
      {% for game in games %}
      <a class="game" href="{{ url_for('game_file', filename=game) }}"><span>🎮 &nbsp; {{ game }}</span><span aria-hidden="true">→</span></a>
      {% else %}
      <div class="empty">Házirshe oyın joq. HTML oyın faylların <code>game</code> papkasına jaylastırıń — olar usı jerde avtomat túrde kórinedi.</div>
      {% endfor %}
    </div>
    <a class="back" href="/portfolio-winter2">← Portfolioga qaytıw</a>
  </main>
  <div id="game-cursor" aria-hidden="true"></div>
  <div id="game-cursor-ring" aria-hidden="true"></div>
  <script>
    const cursorDot = document.getElementById("game-cursor");
    const cursorRing = document.getElementById("game-cursor-ring");
    document.addEventListener("pointermove", event => {
      if (event.pointerType !== "mouse") return;
      const x = `${event.clientX}px`, y = `${event.clientY}px`;
      cursorDot.style.left = x;
      cursorDot.style.top = y;
      cursorRing.style.left = x;
      cursorRing.style.top = y;
    });
    const isCursorTarget = target => target instanceof Element && target.closest("a");
    document.addEventListener("pointerover", event => {
      if (event.pointerType === "mouse" && isCursorTarget(event.target)) document.body.classList.add("game-cursor-hover");
    });
    document.addEventListener("pointerout", event => {
      if (event.pointerType === "mouse" && isCursorTarget(event.target) && !isCursorTarget(event.relatedTarget)) document.body.classList.remove("game-cursor-hover");
    });
  </script>
</body>
</html>""",
        games=games,
    )


@app.get("/game/<path:filename>")
def game_file(filename):
    response = send_from_directory(GAME_DIR, filename)
    response.headers["Cache-Control"] = "no-store"
    return response


@app.get("/api/health")
def health():
    return jsonify({"status": "islamoqda", "time": int(time.time())})


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
