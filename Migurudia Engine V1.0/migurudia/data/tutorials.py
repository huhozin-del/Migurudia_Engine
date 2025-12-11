"""tutorials content data - Complete Rich Text Version"""

TUTORIALS_DATA = {
    "en": {
        "🐍 Python Basics": """# 🐍 Python Basics
## First time coding? Start here!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📦 Variables

Think of a variable as a **labeled box**:

```
    ┌─────────┐
    │   12    │  ← stuff inside
    └─────────┘
       age       ← label on the box
```

Code:
```
age = 12
name = "Tom"
```

The box can change (that's why it's called $$"variable"$$!):
```
age = 12
age = 13    # Tom had a birthday! 🎂
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔢 Data Types

`10`        →  **int** (whole numbers)
`3.14`      →  **float** (decimal numbers)
`"Hello"`   →  **str** (text - use quotes!)
`True`      →  **bool** (yes or no)
`[1,2,3]`   →  **list** (multiple items)
`{"a": 1}`  →  **dict** (key-value pairs)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔀 If Statements

Make decisions:

```
if score >= 60:
    print("You passed! 🎉")
elif score >= 40:
    print("Almost there!")
else:
    print("Try again!")
```

??`elif` = "else if" - check another condition??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔁 Loops

**For loop** - repeat a known number of times:
```
for i in range(3):
    print(i)

# Output: 0, 1, 2
```

!!⚠️ Computers count from 0, not 1!!!

**While loop** - repeat until condition is false:
```
count = 0
while count < 3:
    print(count)
    count += 1
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔧 Functions

Your own **reusable tool**:

```
def say_hi(name):
    print("Hi", name)

say_hi("Tom")    # Hi Tom
say_hi("Amy")    # Hi Amy
```

**Return a value:**
```
def add(a, b):
    return a + b

result = add(3, 5)  # result = 8
```

??Build once, use forever!??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📝 Lists

Multiple things in one place:

```
fruits = ["apple", "banana", "orange"]
#            0         1         2

print(fruits[0])       # apple
print(fruits[-1])      # orange (last item)
print(len(fruits))     # 3

fruits.append("grape") # add to end
fruits.remove("banana") # remove item
```

**Loop through a list:**
```
for fruit in fruits:
    print(fruit)
```

??**List vs Array:** In Python, List can hold mixed types. 
Array (from `numpy`) is for math/science with same-type data.
For games, just use List!??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📖 Dictionaries

Store data with **names** (keys):

```
player = {
    "name": "Hero",
    "health": 100,
    "x": 400
}

print(player["name"])     # Hero
player["health"] -= 10    # take damage
player["score"] = 0       # add new key
```

??Like a real dictionary: look up a word (key) → get meaning (value)??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### ✏️ Comments

Notes the computer ignores:

```
# This is a comment
speed = 5  # Computer skips this text
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

++✅ You're ready! Move on to "Classes 101"++
""",


        "🏗️ Classes 101": """# 🏗️ Classes 101
## Organize your code like a pro!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🤔 Why Classes?

Without classes (messy):
```
player1_x = 100
player1_y = 200
player1_health = 100

player2_x = 500
player2_y = 200
player2_health = 100

# Want 10 players? Copy-paste 30 lines? 😱
```

With classes (clean):
```
player1 = Player(100, 200)
player2 = Player(500, 200)
# Want 10 players? Easy!
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎯 What is a Class?

A class is a **blueprint** (template):

```
┌─────────────────────────────────┐
│  Class: Player (Blueprint)      │
│  ─────────────────────────────  │
│  Data:     x, y, health         │
│  Actions:  move(), take_damage()│
└─────────────────────────────────┘
        │
        │ create instances
        ▼
┌──────────┐  ┌──────────┐  ┌──────────┐
│ player1  │  │ player2  │  │ player3  │
│ x=100    │  │ x=500    │  │ x=300    │
│ y=200    │  │ y=200    │  │ y=400    │
└──────────┘  └──────────┘  └──────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📝 Basic Class

```
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def take_damage(self, amount):
        self.health -= amount

# Create players
player1 = Player(100, 200)
player2 = Player(500, 200)

# Use them
player1.move(10, 0)
player1.take_damage(20)
print(player1.health)  # 80
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔍 Understanding the Parts

**`class Player:`** - Define a new type called "Player"

**`def __init__(self, x, y):`** - Constructor (runs when you create one)
```
player1 = Player(100, 200)
                  ↑    ↑
                  x    y  (these go to __init__)
```

**`self`** - Refers to "this specific instance"
```
player1.x  →  self.x of player1  →  100
player2.x  →  self.x of player2  →  500
```

**`self.x = x`** - Store x as this player's property

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎮 Game Example

```
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
    
    def chase(self, player):
        if self.x < player.x:
            self.x += self.speed
        elif self.x > player.x:
            self.x -= self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), 
                         (self.x, self.y, 40, 40))

# Create enemies
enemies = [
    Enemy(100, 100),
    Enemy(700, 300),
    Enemy(400, 400)
]

# In game_loop:
for enemy in enemies:
    enemy.chase(player)
    enemy.draw(screen)
```

++No more `enemy1_x`, `enemy2_x`... just a clean list!++

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🆚 Global Variables vs Class

!!❌ Global variables (bad):!!
```
player_x = 400
player_y = 300

def move_player():
    global player_x, player_y  # Need this everywhere!
    player_x += 5
```

++✅ Class (good):++
```
class Player:
    def __init__(self):
        self.x = 400
        self.y = 300
    
    def move(self):
        self.x += 5  # No global needed!

player = Player()
player.move()
```

??With classes, data and functions stay together.
No `global` needed because `self` keeps track!??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📦 When to Use Classes?

Use a class when you have:
  • **Multiple similar things** (players, enemies, bullets)
  • **Data + actions together** (player has x, y AND can move)
  • **State that changes** (health goes up/down)

Don't bother for:
  • Simple scripts
  • One-off calculations
  • Things that don't have state

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🏆 Challenge

Convert this messy code:
```
bullet1_x = 100
bullet1_y = 200
bullet1_speed = 10

bullet2_x = 200
bullet2_y = 200
bullet2_speed = 10
```

Into a clean `Bullet` class!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

++✅ Now you understand classes! Next: "Getting Started"++
""",


        "🚀 Getting Started": """# 🚀 Getting Started
## Your first game in 2 minutes!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎯 The Magic Formula

Every game needs this:

```
def game_loop(screen, events):
    screen.fill((0, 0, 0))
    # your code here!
```

??That's the skeleton. Let's fill it in!??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎨 Try This Now!

Copy this, click **Run**:

```
def game_loop(screen, events):
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (400, 240), 50)
```

++You should see a red circle! 🔴++

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎨 Colors = (R, G, B)

Mix red, green, blue (**0-255** each):

`(255, 0, 0)`      →  🔴 **Red**
`(0, 255, 0)`      →  🟢 **Green**
`(0, 0, 255)`      →  🔵 **Blue**
`(255, 255, 0)`    →  🟡 **Yellow**
`(255, 128, 0)`    →  🟠 **Orange**
`(128, 0, 255)`    →  🟣 **Purple**
`(255, 255, 255)`  →  ⚪ **White**
`(0, 0, 0)`        →  ⚫ **Black**
`(128, 128, 128)`  →  🔘 **Gray**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 💡 What's Happening?

??`game_loop` runs **60 times per second**!??

```
┌──────────────────────────────────┐
│  screen.fill() ← paint background│
│  draw stuff    ← draw on top     │
│  (repeat 60x per second)         │
└──────────────────────────────────┘
```

This creates the illusion of movement - like a flipbook!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📐 Screen Coordinates

```
(0,0) ────────────────────→ X (854)
  │
  │      (400, 240)
  │          •  ← center-ish
  │
  ▼
  Y (480)
```

??Top-left is (0,0), not bottom-left like in math class!??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🏆 Challenge

Change the color! Try making:
  • A $$blue$$ circle
  • A $$bigger$$ circle (change 50 to 100)
  • $$Move it$$ (change 400, 240)
  • Draw $$two$$ circles!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

++✅ Next: "Drawing Shapes"++
""",


        "🔷 Drawing Shapes": """# 🔷 Drawing Shapes
## Rectangles, circles, lines!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### ⬜ Rectangle

```
pygame.draw.rect(screen, COLOR, (x, y, width, height))
```

```
    (x,y)
      ↓
      ┌─────────────┐
      │             │ height
      └─────────────┘
           width
```

Example:
```
pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150))
```

**Filled vs Outline:**
```
# Filled (default)
pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150))

# Outline only (add width parameter)
pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150), 3)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### ⚫ Circle

```
pygame.draw.circle(screen, COLOR, (center_x, center_y), radius)
```

```
         ╭───╮
        │  •  │  ← (x,y) is the CENTER
         ╰───╯
          radius
```

Example:
```
pygame.draw.circle(screen, (0, 255, 0), (400, 240), 80)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📏 Line

```
pygame.draw.line(screen, COLOR, (x1, y1), (x2, y2), thickness)
```

```
(x1,y1) •─────────────• (x2,y2)
```

Example:
```
pygame.draw.line(screen, (0, 0, 255), (50, 50), (300, 200), 5)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔶 Other Shapes

**Ellipse (oval):**
```
pygame.draw.ellipse(screen, (255, 255, 0), (100, 100, 200, 100))
```

**Polygon (any shape):**
```
points = [(100, 100), (150, 50), (200, 100)]
pygame.draw.polygon(screen, (255, 0, 255), points)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎨 Complete Example

```
def game_loop(screen, events):
    screen.fill((30, 30, 30))
    
    # Red rectangle
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150))
    
    # Green circle
    pygame.draw.circle(screen, (0, 255, 0), (500, 200), 80)
    
    # Blue line
    pygame.draw.line(screen, (0, 0, 255), (50, 400), (800, 400), 5)
    
    # Yellow ellipse
    pygame.draw.ellipse(screen, (255, 255, 0), (600, 300, 100, 60))
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

??💡 TIP: Drawing order matters! Things drawn LATER appear ON TOP.??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🏆 Challenge

Draw a simple **face** using:
  • 1 big circle (head)
  • 2 small circles (eyes)
  • 1 line or arc (mouth)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

++✅ Next: "Keyboard Input"++
""",


        "⌨️ Keyboard Input": """# ⌨️ Keyboard Input
## Make things move!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎮 The Idea

```
keys = pygame.key.get_pressed()

if keys[pygame.K_LEFT]:
    # move left!
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🕹️ Moving a Player

```
player_x = 400
player_y = 240

def game_loop(screen, events):
    global player_x, player_y
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:  player_x -= 5
    if keys[pygame.K_RIGHT]: player_x += 5
    if keys[pygame.K_UP]:    player_y -= 5
    if keys[pygame.K_DOWN]:  player_y += 5
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, 50, 50))
```

++Copy this and try it! Use arrow keys to move. 🎮++

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### ❓ Why "global"?

Without it, Python thinks you're making a **NEW** variable
inside the function, not changing the outside one.

```
player_x = 400          ← outside

def game_loop(...):
    global player_x     ← "I mean THAT one!"
    player_x -= 5       ← now it works
```

??Better solution: Use a class! (See "Classes 101")??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎹 Common Keys

`pygame.K_LEFT`   →  ← Arrow
`pygame.K_RIGHT`  →  → Arrow
`pygame.K_UP`     →  ↑ Arrow
`pygame.K_DOWN`   →  ↓ Arrow
`pygame.K_SPACE`  →  Spacebar
`pygame.K_RETURN` →  Enter
`pygame.K_ESCAPE` →  Escape
`pygame.K_a`      →  A key
`pygame.K_w`      →  W key

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔘 Single Press vs Held Down

`get_pressed()` = currently held down (for movement)
`KEYDOWN event` = pressed once (for jumping, shooting)

```
def game_loop(screen, events):
    # Held down - for smooth movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    
    # Single press - for actions
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()  # Only triggers once per press
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🏆 Challenge

  • Change speed (try `10` instead of `5`)
  • Use **WASD** keys instead of arrows
  • Change the player $$color$$ when moving

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

++✅ Next: "Loading Images"++
""",


        "🖼️ Loading Images": """# 🖼️ Loading Images
## Use your own pictures!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📥 Easy Way (Recommended!)

1. Click **"Asset"** menu
2. Click **"Import Image"**
3. Pick your image
4. ++Code appears automatically! ✨++

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📝 Manual Way

```
# Load image (do this OUTSIDE game_loop!)
player_img = pygame.image.load(r"player.png")

def game_loop(screen, events):
    screen.fill((0, 0, 0))
    screen.blit(player_img, (100, 100))
```

??`screen.blit(image, position)` = draw image at position??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📐 Resize Image

```
player_img = pygame.image.load(r"player.png")
player_img = pygame.transform.scale(player_img, (64, 64))
```
                                                  ↑    ↑
                                               width  height

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔄 Rotate & Flip

```
# Rotate (degrees, counter-clockwise)
rotated = pygame.transform.rotate(player_img, 45)

# Flip horizontally
flipped = pygame.transform.flip(player_img, True, False)
                                              ↑      ↑
                                          flip_x  flip_y
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### ⚠️ Common Mistakes

!!❌ Loading inside game_loop (super slow!)!!
++✅ Load ONCE, outside, at the top++

!!❌ Wrong file path!!
++✅ Put image in same folder, use just the filename++

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 💡 Tips

??• Use **PNG** for transparency??
??• The `r` in `r"path"` prevents errors on Windows??
??• Keep images small for better performance??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

++✅ Next: "Playing Sounds"++
""",


        "🔊 Playing Sounds": """# 🔊 Playing Sounds
## Add music and sound effects!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📥 Easy Way

1. Click **"Asset"** menu
2. Click **"Import Sound"**
3. ++Done! ✨++

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔈 Sound Effects

Short sounds (jumps, hits, coins):

```
# Load once at the top
jump = pygame.mixer.Sound(r"jump.wav")

# Play it anywhere
jump.play()
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎵 Background Music

Long audio (music):

```
pygame.mixer.music.load(r"music.mp3")

pygame.mixer.music.play(-1)   # -1 = loop forever
pygame.mixer.music.play(0)    # play once
pygame.mixer.music.stop()     # stop
pygame.mixer.music.pause()    # pause
pygame.mixer.music.unpause()  # resume
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎚️ Volume

```
jump.set_volume(0.5)                # 50%
pygame.mixer.music.set_volume(0.3)  # 30%
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎮 Play Sound on Key Press

```
jump = pygame.mixer.Sound(r"jump.wav")

def game_loop(screen, events):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump.play()  # Boing! 🐰
    
    screen.fill((0, 0, 0))
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 💡 Supported Formats

`.wav`  ←  ??best for sound effects??
`.mp3`  ←  ??good for music??
`.ogg`  ←  ??works great, smaller files??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

++✅ Next: "Collision Detection"++
""",


        "💥 Collision Detection": """# 💥 Collision Detection
## Know when things touch!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎯 The Idea

```
    ┌─────┐
    │  A  │───┐
    └─────┘   │  ← Are they touching?
         ┌────┴┐
         │  B  │
         └─────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📦 Rectangle Collision

```
# Create invisible boxes around objects
player_rect = pygame.Rect(player_x, player_y, 50, 50)
enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 50)

# Check if they touch
if player_rect.colliderect(enemy_rect):
    print("BOOM! 💥")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📐 pygame.Rect Properties

```
rect = pygame.Rect(100, 200, 50, 30)
                    ↑    ↑   ↑   ↑
                    x    y   w   h

rect.x, rect.y           # position
rect.width, rect.height  # size
rect.centerx, rect.centery  # center point
rect.top, rect.bottom    # edges
rect.left, rect.right
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎮 Complete Game Example

```
player_x, player_y = 400, 300
enemy_x, enemy_y = 200, 200
score = 0

def game_loop(screen, events):
    global player_x, player_y, enemy_x, enemy_y, score
    
    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player_x -= 5
    if keys[pygame.K_RIGHT]: player_x += 5
    if keys[pygame.K_UP]:    player_y -= 5
    if keys[pygame.K_DOWN]:  player_y += 5
    
    # Check collision
    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 50)
    
    if player_rect.colliderect(enemy_rect):
        score += 1
        enemy_x = random.randint(50, 750)
        enemy_y = random.randint(50, 400)
    
    # Draw
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player_rect)
    pygame.draw.rect(screen, (255, 0, 0), enemy_rect)
```

++This is a real game! Catch the red squares. 🎯++

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 💡 Keep Player on Screen

```
# Clamp to screen boundaries
if player_x < 0: player_x = 0
if player_x > 854 - 50: player_x = 854 - 50
if player_y < 0: player_y = 0
if player_y > 480 - 50: player_y = 480 - 50
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

++✅ Next: "Exporting Your Game"++
""",


        "📦 Export Game": """# 📦 Exporting Your Game
## Share your creation with the world!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🐍 Export as Python (.py)

1. Click **"Export"** → **"Export as Python"**
2. Choose where to save
3. Share the `.py` file!

!!⚠️ Others need Python + Pygame installed!!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 💻 Export as EXE (.exe)

1. Click **"Export"** → **"Export as EXE"**
2. Wait 1-2 minutes ☕
3. Share the `.exe` file!

++✅ No Python needed! Just double-click and play!++

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📁 Don't Forget Your Assets!

```
📂 MyGame/
   ├── game.exe      ← your game
   ├── player.png    ← include these!
   ├── enemy.png
   └── jump.wav
```

??Put assets NEXT TO your game file.??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔧 Troubleshooting

!!"Can't find image/sound!"!!
  → Put assets in same folder as game
  → Use simple names: `"player.png"`

!!"EXE is 50MB!"!!
  → Normal! It includes Python itself.

!!"Antivirus blocks it!"!!
  → It's safe, just not signed. Click "Run anyway"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 🎉 Congratulations!

$$You've learned everything you need.$$
$$Now go make something awesome!$$
"""
    },


    "zh": {
        "🐍 Python 基础": """# 🐍 Python 基础
## 第一次写代码？从这里开始！

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📦 变量

把变量想象成一个**贴了标签的盒子**：

```
    ┌─────────┐
    │   12    │  ← 盒子里的东西
    └─────────┘
       age       ← 盒子上的标签
```

代码：
```
age = 12
name = "小明"
```

盒子里的东西可以换（所以叫$$"变"量$$！）：
```
age = 12
age = 13    # 小明过生日啦！🎂
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔢 数据类型

`10`        →  **int** (整数)
`3.14`      →  **float** (小数)
`"你好"`    →  **str** (文字，要用引号！)
`True`      →  **bool** (是 或 否)
`[1,2,3]`   →  **list** (列表)
`{"a": 1}`  →  **dict** (字典)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔀 判断 if

做决定：

```
if score >= 60:
    print("及格啦！🎉")
elif score >= 40:
    print("差一点点！")
else:
    print("再加油！")
```

??`elif` = "else if" - 再检查另一个条件??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔁 循环

**for 循环** - 重复固定次数：
```
for i in range(3):
    print(i)

# 输出：0, 1, 2
```

!!⚠️ 电脑从 0 开始数，不是从 1！!!

**while 循环** - 条件满足就一直重复：
```
count = 0
while count < 3:
    print(count)
    count += 1
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔧 函数

自己造一个**可重复使用的工具**：

```
def say_hi(name):
    print("你好", name)

say_hi("小明")    # 你好 小明
say_hi("小红")    # 你好 小红
```

**返回值：**
```
def add(a, b):
    return a + b

result = add(3, 5)  # result = 8
```

??造一次，用无数次！??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📝 列表 List

很多东西放一起：

```
fruits = ["苹果", "香蕉", "橘子"]
#           0       1       2

print(fruits[0])       # 苹果
print(fruits[-1])      # 橘子（最后一个）
print(len(fruits))     # 3

fruits.append("西瓜")  # 加到最后
fruits.remove("香蕉")  # 删掉某个
```

**遍历列表：**
```
for fruit in fruits:
    print(fruit)
```

??**List vs Array：** Python 的 List 可以放不同类型的东西。
Array（来自 `numpy`）是给数学/科学计算用的，只能放同类型。
做游戏用 List 就够了！??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📖 字典 Dictionary

用**名字**（键）存数据：

```
player = {
    "name": "英雄",
    "health": 100,
    "x": 400
}

print(player["name"])     # 英雄
player["health"] -= 10    # 受伤
player["score"] = 0       # 添加新的键
```

??就像查字典：查一个词（键）→ 得到解释（值）??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### ✏️ 注释

写给自己看的笔记，电脑会跳过：

```
# 这是注释
speed = 5  # 电脑不管这段文字
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

++✅ 准备好了！去看下一个："类 Class 入门"++
""",


        "🏗️ 类 Class 入门": """# 🏗️ 类 Class 入门
## 像专业程序员一样组织代码！

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🤔 为什么要用类？

没有类（乱）：
```
player1_x = 100
player1_y = 200
player1_health = 100

player2_x = 500
player2_y = 200
player2_health = 100

# 想要 10 个玩家？复制粘贴 30 行？😱
```

有类（整齐）：
```
player1 = Player(100, 200)
player2 = Player(500, 200)
# 想要 10 个？轻松！
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎯 什么是类？

类就是一个**蓝图**（模板）：

```
┌─────────────────────────────────┐
│  类：Player（蓝图）              │
│  ─────────────────────────────  │
│  数据：    x, y, health         │
│  动作：    move(), take_damage()│
└─────────────────────────────────┘
        │
        │ 创建实例
        ▼
┌──────────┐  ┌──────────┐  ┌──────────┐
│ player1  │  │ player2  │  │ player3  │
│ x=100    │  │ x=500    │  │ x=300    │
│ y=200    │  │ y=200    │  │ y=400    │
└──────────┘  └──────────┘  └──────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📝 基本写法

```
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def take_damage(self, amount):
        self.health -= amount

# 创建玩家
player1 = Player(100, 200)
player2 = Player(500, 200)

# 使用它们
player1.move(10, 0)
player1.take_damage(20)
print(player1.health)  # 80
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔍 理解每个部分

**`class Player:`** - 定义一个叫 "Player" 的新类型

**`def __init__(self, x, y):`** - 构造函数（创建时运行）
```
player1 = Player(100, 200)
                  ↑    ↑
                  x    y  （这两个传给 __init__）
```

**`self`** - 指"这个具体的实例"
```
player1.x  →  player1 的 self.x  →  100
player2.x  →  player2 的 self.x  →  500
```

**`self.x = x`** - 把 x 存成这个玩家的属性

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎮 游戏示例

```
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
    
    def chase(self, player):
        if self.x < player.x:
            self.x += self.speed
        elif self.x > player.x:
            self.x -= self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), 
                         (self.x, self.y, 40, 40))

# 创建敌人
enemies = [
    Enemy(100, 100),
    Enemy(700, 300),
    Enemy(400, 400)
]

# 在 game_loop 里：
for enemy in enemies:
    enemy.chase(player)
    enemy.draw(screen)
```

++不用再写 `enemy1_x`, `enemy2_x`... 一个列表搞定！++

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🆚 全局变量 vs 类

!!❌ 全局变量（不好）：!!
```
player_x = 400
player_y = 300

def move_player():
    global player_x, player_y  # 到处都要写这个！
    player_x += 5
```

++✅ 类（好）：++
```
class Player:
    def __init__(self):
        self.x = 400
        self.y = 300
    
    def move(self):
        self.x += 5  # 不用 global！

player = Player()
player.move()
```

??用类的话，数据和函数在一起。
不用 `global` 因为 `self` 会记住！??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📦 什么时候用类？

适合用类：
  • **多个类似的东西**（玩家、敌人、子弹）
  • **数据 + 动作 在一起**（玩家有 x, y 而且能移动）
  • **状态会变化**（血量上下浮动）

不用类也行：
  • 简单脚本
  • 一次性计算
  • 没有状态的东西

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🏆 小挑战

把这堆乱七八糟的代码：
```
bullet1_x = 100
bullet1_y = 200
bullet1_speed = 10

bullet2_x = 200
bullet2_y = 200
bullet2_speed = 10
```

改成一个整洁的 `Bullet` 类！

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

++✅ 现在你懂类了！下一个："入门指南"++
""",


        "🚀 入门指南": """# 🚀 入门指南
## 2 分钟做出你的第一个游戏！

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎯 核心公式

每个游戏都需要这个：

```
def game_loop(screen, events):
    screen.fill((0, 0, 0))
    # 你的代码写这里！
```

??这是骨架，我们来填肉！??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎨 现在就试试！

复制这段代码，点击**运行**：

```
def game_loop(screen, events):
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (400, 240), 50)
```

++你会看到一个红色圆圈！🔴++

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎨 颜色 = (红, 绿, 蓝)

三种颜色混合，每个 **0-255**：

`(255, 0, 0)`      →  🔴 **红色**
`(0, 255, 0)`      →  🟢 **绿色**
`(0, 0, 255)`      →  🔵 **蓝色**
`(255, 255, 0)`    →  🟡 **黄色**
`(255, 128, 0)`    →  🟠 **橙色**
`(128, 0, 255)`    →  🟣 **紫色**
`(255, 255, 255)`  →  ⚪ **白色**
`(0, 0, 0)`        →  ⚫ **黑色**
`(128, 128, 128)`  →  🔘 **灰色**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 💡 发生了什么？

??`game_loop` **每秒运行 60 次**！??

```
┌──────────────────────────────────┐
│  screen.fill()  ← 画背景         │
│  画东西         ← 画在上面        │
│  （每秒重复 60 次）               │
└──────────────────────────────────┘
```

这样就产生了动画效果——就像翻书动画！

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📐 屏幕坐标

```
(0,0) ────────────────────→ X (854)
  │
  │      (400, 240)
  │          •  ← 大约在中间
  │
  ▼
  Y (480)
```

??左上角是 (0,0)，不是左下角（和数学课不一样）！??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🏆 小挑战

改一改颜色！试试：
  • 画一个$$蓝色$$圆
  • 画一个$$大一点的$$圆（把 50 改成 100）
  • $$移动位置$$（改 400, 240）
  • 画$$两个$$圆！

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

++✅ 下一个："绘制图形"++
""",


        "🔷 绘制图形": """# 🔷 绘制图形
## 矩形、圆形、线条！

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### ⬜ 矩形

```
pygame.draw.rect(screen, 颜色, (x, y, 宽, 高))
```

```
    (x,y)
      ↓
      ┌─────────────┐
      │             │ 高
      └─────────────┘
           宽
```

例子：
```
pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150))
```

**填充 vs 边框：**
```
# 填充（默认）
pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150))

# 只有边框（加上线宽参数）
pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150), 3)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### ⚫ 圆形

```
pygame.draw.circle(screen, 颜色, (圆心x, 圆心y), 半径)
```

```
         ╭───╮
        │  •  │  ← (x,y) 是圆心
         ╰───╯
          半径
```

例子：
```
pygame.draw.circle(screen, (0, 255, 0), (400, 240), 80)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📏 线条

```
pygame.draw.line(screen, 颜色, (x1, y1), (x2, y2), 粗细)
```

```
(x1,y1) •─────────────• (x2,y2)
```

例子：
```
pygame.draw.line(screen, (0, 0, 255), (50, 50), (300, 200), 5)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔶 其他形状

**椭圆：**
```
pygame.draw.ellipse(screen, (255, 255, 0), (100, 100, 200, 100))
```

**多边形：**
```
points = [(100, 100), (150, 50), (200, 100)]
pygame.draw.polygon(screen, (255, 0, 255), points)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎨 完整例子

```
def game_loop(screen, events):
    screen.fill((30, 30, 30))
    
    # 红色方块
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 150))
    
    # 绿色圆
    pygame.draw.circle(screen, (0, 255, 0), (500, 200), 80)
    
    # 蓝色线
    pygame.draw.line(screen, (0, 0, 255), (50, 400), (800, 400), 5)
    
    # 黄色椭圆
    pygame.draw.ellipse(screen, (255, 255, 0), (600, 300, 100, 60))
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

??💡 提示：画的顺序很重要！后画的会覆盖先画的。??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🏆 小挑战

用这些画一个简单的**脸**：
  • 1 个大圆（脸）
  • 2 个小圆（眼睛）
  • 1 条线或弧线（嘴巴）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

++✅ 下一个："键盘输入"++
""",


        "⌨️ 键盘输入": """# ⌨️ 键盘输入
## 让东西动起来！

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎮 核心思路

```
keys = pygame.key.get_pressed()

if keys[pygame.K_LEFT]:
    # 往左移动！
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🕹️ 移动方块

```
player_x = 400
player_y = 240

def game_loop(screen, events):
    global player_x, player_y
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:  player_x -= 5
    if keys[pygame.K_RIGHT]: player_x += 5
    if keys[pygame.K_UP]:    player_y -= 5
    if keys[pygame.K_DOWN]:  player_y += 5
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, 50, 50))
```

++复制试试！用方向键移动。🎮++

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### ❓ 为什么要写 "global"？

不写的话，Python 以为你要在函数里面**新建**一个变量，
而不是修改外面那个。

```
player_x = 400          ← 外面的变量

def game_loop(...):
    global player_x     ← "我说的是那个！"
    player_x -= 5       ← 现在才能改
```

??更好的方案：用类！（看"类 Class 入门"）??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎹 常用按键

`pygame.K_LEFT`   →  ← 左
`pygame.K_RIGHT`  →  → 右
`pygame.K_UP`     →  ↑ 上
`pygame.K_DOWN`   →  ↓ 下
`pygame.K_SPACE`  →  空格
`pygame.K_RETURN` →  回车
`pygame.K_ESCAPE` →  ESC
`pygame.K_a`      →  A 键
`pygame.K_w`      →  W 键

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔘 单次按下 vs 持续按住

`get_pressed()` = 当前按住（用于移动）
`KEYDOWN 事件` = 按一次触发一次（用于跳跃、射击）

```
def game_loop(screen, events):
    # 按住 - 平滑移动
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    
    # 单次按下 - 动作
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()  # 只触发一次
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🏆 小挑战

  • 改速度（把 `5` 改成 `10`）
  • 用 **WASD** 代替方向键
  • 移动时改变$$颜色$$

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

++✅ 下一个："加载图片"++
""",


        "🖼️ 加载图片": """# 🖼️ 加载图片
## 用你自己的图片！

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📥 简单方法（推荐！）

1. 点击**"资源"**菜单
2. 点击**"导入图片"**
3. 选择图片
4. ++代码自动出现！✨++

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📝 手动方法

```
# 加载图片（写在 game_loop 外面！）
player_img = pygame.image.load(r"player.png")

def game_loop(screen, events):
    screen.fill((0, 0, 0))
    screen.blit(player_img, (100, 100))
```

??`screen.blit(图片, 位置)` = 在某个位置画图片??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📐 调整大小

```
player_img = pygame.image.load(r"player.png")
player_img = pygame.transform.scale(player_img, (64, 64))
```
                                                  ↑    ↑
                                                 宽   高

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔄 旋转和翻转

```
# 旋转（角度，逆时针）
rotated = pygame.transform.rotate(player_img, 45)

# 水平翻转
flipped = pygame.transform.flip(player_img, True, False)
                                              ↑      ↑
                                          水平翻转 垂直翻转
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### ⚠️ 常见错误

!!❌ 在 game_loop 里面加载（超级慢！）!!
++✅ 只加载一次，写在外面++

!!❌ 路径写错了!!
++✅ 把图片放同一个文件夹，只写文件名++

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 💡 小提示

??• **PNG** 格式支持透明??
??• `r"路径"` 前面的 r 防止路径出错??
??• 图片小一点性能更好??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

++✅ 下一个："播放音效"++
""",


        "🔊 播放音效": """# 🔊 播放音效
## 加入音乐和音效！

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📥 简单方法

1. 点击**"资源"**菜单
2. 点击**"导入音频"**
3. ++搞定！✨++

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔈 音效

短声音（跳跃、碰撞、金币）：

```
# 在顶部加载一次
jump = pygame.mixer.Sound(r"jump.wav")

# 任何地方播放
jump.play()
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎵 背景音乐

长音频（音乐）：

```
pygame.mixer.music.load(r"music.mp3")

pygame.mixer.music.play(-1)   # -1 = 循环播放
pygame.mixer.music.play(0)    # 播放一次
pygame.mixer.music.stop()     # 停止
pygame.mixer.music.pause()    # 暂停
pygame.mixer.music.unpause()  # 继续
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎚️ 音量

```
jump.set_volume(0.5)                # 50%
pygame.mixer.music.set_volume(0.3)  # 30%
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎮 按键播放音效

```
jump = pygame.mixer.Sound(r"jump.wav")

def game_loop(screen, events):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump.play()  # 蹦！🐰
    
    screen.fill((0, 0, 0))
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 💡 支持的格式

`.wav`  ←  ??音效最佳??
`.mp3`  ←  ??音乐可以??
`.ogg`  ←  ??也行，文件更小??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

++✅ 下一个："碰撞检测"++
""",


        "💥 碰撞检测": """# 💥 碰撞检测
## 知道东西什么时候碰到了！

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎯 核心思路

```
    ┌─────┐
    │  A  │───┐
    └─────┘   │  ← 它们碰到了吗？
         ┌────┴┐
         │  B  │
         └─────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📦 矩形碰撞

```
# 给物体套一个隐形的框
player_rect = pygame.Rect(player_x, player_y, 50, 50)
enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 50)

# 检测是否碰撞
if player_rect.colliderect(enemy_rect):
    print("撞上了！💥")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📐 pygame.Rect 属性

```
rect = pygame.Rect(100, 200, 50, 30)
                    ↑    ↑   ↑   ↑
                    x    y   宽  高

rect.x, rect.y           # 位置
rect.width, rect.height  # 大小
rect.centerx, rect.centery  # 中心点
rect.top, rect.bottom    # 边缘
rect.left, rect.right
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🎮 完整小游戏

```
player_x, player_y = 400, 300
enemy_x, enemy_y = 200, 200
score = 0

def game_loop(screen, events):
    global player_x, player_y, enemy_x, enemy_y, score
    
    # 移动玩家
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player_x -= 5
    if keys[pygame.K_RIGHT]: player_x += 5
    if keys[pygame.K_UP]:    player_y -= 5
    if keys[pygame.K_DOWN]:  player_y += 5
    
    # 检测碰撞
    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 50)
    
    if player_rect.colliderect(enemy_rect):
        score += 1
        enemy_x = random.randint(50, 750)
        enemy_y = random.randint(50, 400)
    
    # 绘制
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player_rect)
    pygame.draw.rect(screen, (255, 0, 0), enemy_rect)
```

++这是个真游戏！去抓红色方块。🎯++

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 💡 别让玩家跑出屏幕

```
# 限制在屏幕范围内
if player_x < 0: player_x = 0
if player_x > 854 - 50: player_x = 854 - 50
if player_y < 0: player_y = 0
if player_y > 480 - 50: player_y = 480 - 50
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

++✅ 下一个："导出游戏"++
""",


        "📦 导出游戏": """# 📦 导出游戏
## 把你的作品分享给全世界！

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🐍 导出为 Python (.py)

1. 点击**"导出"** → **"导出为 Python"**
2. 选择保存位置
3. 把 `.py` 文件分享出去！

!!⚠️ 别人需要安装 Python + Pygame!!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 💻 导出为 EXE (.exe)

1. 点击**"导出"** → **"导出为 EXE"**
2. 等 1-2 分钟 ☕
3. 把 `.exe` 文件分享出去！

++✅ 不用装任何东西！双击就能玩！++

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 📁 别忘了你的素材！

```
📂 我的游戏/
   ├── game.exe      ← 你的游戏
   ├── player.png    ← 这些也要带上！
   ├── enemy.png
   └── jump.wav
```

??把素材放在游戏旁边。??

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 🔧 常见问题

!!"找不到图片/音效！"!!
  → 把素材放在游戏同一个文件夹
  → 用简单的名字：`"player.png"`

!!"EXE 有 50MB！"!!
  → 正常的！里面包含了 Python 本身。

!!"杀毒软件拦截了！"!!
  → 它是安全的，只是没有签名。点"仍然运行"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 🎉 恭喜你！

$$你已经学会了所有需要的东西。$$
$$现在去做点厉害的吧！$$
"""
    }
}


def get_tutorial_titles(lang: str) -> list:
    """get tutorial titles for current language"""
    return list(TUTORIALS_DATA.get(lang, TUTORIALS_DATA["en"]).keys())


def get_tutorial_content(lang: str, title: str) -> str:
    """get tutorial content by title"""
    return TUTORIALS_DATA.get(lang, TUTORIALS_DATA["en"]).get(
        title, "Tutorial not found."
    )