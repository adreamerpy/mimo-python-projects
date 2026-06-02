import pygame
import random
import math

# የፒኬም ዝግጅት
pygame.init()
screen = pygame.display.set_mode((800, 600))

# ነጥቦችን በፍጥነት እና በመገኛ መፍጠር
nodes = []
for _ in range(30):
    nodes.append({
        'x': random.randint(0, 800), 
        'y': random.randint(0, 600),
        'vx': random.uniform(-1, 1), # የX ፍጥነት
        'vy': random.uniform(-1, 1)  # የY ፍጥነት
    })

running = True
while running:
    screen.fill((0, 0, 0)) # ዳራውን ማጽዳት
    
    # የነጥቦችን ቦታ ማዘመን
    for node in nodes:
        node['x'] += node['vx']
        node['y'] += node['vy']
        
        # ማያ ገጹን ሲነኩ ወደ ተቃራኒ አቅጣጫ መመለስ
        if node['x'] < 0 or node['x'] > 800: node['vx'] *= -1
        if node['y'] < 0 or node['y'] > 600: node['vy'] *= -1
        
        # ነጥቡን መሳል
        pygame.draw.circle(screen, (0, 255, 255), (int(node['x']), int(node['y'])), 3)

    # በነጥቦች መካከል መስመር መሳል
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            dist = math.hypot(nodes[i]['x'] - nodes[j]['x'], nodes[i]['y'] - nodes[j]['y'])
            if dist < 150: # ነጥቦቹ ከተጠጋጉ መስመር ይሳል
                pygame.draw.line(screen, (0, 100, 100), (nodes[i]['x'], nodes[i]['y']), (nodes[j]['x'], nodes[j]['y']))

    pygame.display.flip()
    pygame.time.Clock().tick(60) # ፍጥነቱን መቆጣጠር