from datatypes import OrderedPair,Body,Universe
import math
import copy


def simulate(initial_universe: Universe, num_gens: int, time: float) -> list[Universe]:
    time_points: list[Universe] = [initial_universe]
    for i in range(1, num_gens + 1):
        next_universe = update_universe(time_points[i - 1], time)
        time_points.append(next_universe)
    return time_points

def update_universe(current_universe: Universe, time: float)->Universe:
    new_universe = copy.deepcopy(current_universe)
    for b in new_universe.bodies:
        old_acc, old_vel = b.acceleration, b.velocity
        b.acceleration = update_acceleration(b, current_universe)
        b.velocity = update_velocity(b, old_acc, time)
        b.position = update_position(b, old_acc, old_vel, time)
    return new_universe

def update_position(b: Body, old_acceleration: OrderedPair, old_velocity: OrderedPair, time: float)->OrderedPair:	
    px = (0.5 * old_acceleration.x * (time**2) + old_velocity.x * time + b.position.x)
    py = (0.5 * old_acceleration.y * (time**2) + old_velocity.y * time + b.position.y)
    return OrderedPair(px,py)
	
def update_velocity(b: Body, old_acceleration: OrderedPair, time: float)->OrderedPair:
    vx = (0.5 * (b.acceleration.x + old_acceleration.x) * time + b.velocity.x)
    vy = (0.5 * (b.acceleration.y + old_acceleration.y) * time + b.velocity.y)
    return OrderedPair(vx,vy)

def update_acceleration(b: Body, current_universe: Universe)->OrderedPair:
    f = compute_net_force(b,current_universe.bodies, current_universe.gravitationalConstant)
    ax = f.x/b.mass
    ay = f.y/b.mass
    return OrderedPair(ax,ay)


def compute_net_force(focus_body: Body, bodies: list[Body], g: float)->OrderedPair:
	nforce = OrderedPair()
	for b in bodies:
		f = compute_force(focus_body,b,g)
		nforce.x += f.x
		nforce.y += f.y
	return nforce


def compute_force(b1: Body, b2: Body, g: float)->OrderedPair:
    force = OrderedPair()
    d = distance(b1,b2)
    if d [2] == 0:
        return force
    else:
        f = (g * b1.mass * b2.mass)/(d[2]**2)
        force.x = f * d[0]/d[2]
        force.y = f * d[1]/d[2]
    return force


def distance(b1: Body, b2: Body)->tuple:
    dx = b2.position.x - b1.position.x
    dy = b2.position.y -b1.position.y
    return (dx,dy,math.sqrt(dx**2 + dy**2))
