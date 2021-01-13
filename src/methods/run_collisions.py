
def run_collisions(balls, areas, centers, pads, borders, width, height, energy_loss, counter):
    i = 0
    used = []

    for ball1 in balls:
        #print(i+1,ball1.angle)        
        j = 0
        for ball2 in balls:
            if i != j and ball1.checkIfCollides(ball2):
                ball1.collision(ball2)
            j+=1
        i+=1
    for ball in balls:
        if ball.x < 0+borders:
            ball.vx *= -1
            ball.vx /= energy_loss
            ball.x = 0+borders
        if ball.y < 0+borders:
            ball.vy *= -1
            ball.vy /= energy_loss
            ball.y = 0+borders
        if ball.x > width-borders:
            ball.vx *= -1
            ball.vx /= energy_loss
            ball.x = width-borders
        if ball.y > height-borders:
            ball.vy *= -1
            ball.vy /= energy_loss
            ball.y = height-borders

        if counter % 5 == 0:
            ball.deflect = False
                
    for area in areas:
        area.apply_forces(balls)

    for center in centers:
        center.apply_forces(balls)

    for pad in pads:
        pad.bounce(balls)