"""Main file for the moving agents simulation."""

import random
import math
import multiprocessing

import numpy as np

WIDTH, HEIGHT = 1000, 1000
AGENT_SIZE = 5
NUM_AGENTS = 100
CIRCLE_SIZE = 50

TIME = 6000

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


def levy_walk(agent, angle, step):

    agent["x"] += step * math.cos(angle)
    agent["y"] += step * math.sin(angle)


def random_walk(agent, angle, step):

    if angle < math.pi / 2:
        agent["x"] += step
    elif angle < math.pi:
        agent["y"] += step
    elif angle < 3 * math.pi / 2:
        agent["x"] -= step
    else:
        agent["y"] -= step


def brownian_motion(agent, angle, step):

    agent["x"] += step * math.cos(angle)
    agent["y"] += step * math.sin(angle)


def main(mode, movement_scale_factor):

    agents = []
    for _ in range(NUM_AGENTS):
        agent = {
            "x": random.randint(0, WIDTH),
            "y": random.randint(0, HEIGHT),
            "step_length": random.uniform(1, 10),
            "angle": random.uniform(0, 2 * math.pi),
            "color": GREEN,
        }
        agents.append(agent)

    if mode == 0:
        step_length = movement_scale_factor
        steps = [step_length] * TIME * NUM_AGENTS
    elif mode == 1:
        beta = movement_scale_factor / (movement_scale_factor - 1)
        steps = np.random.pareto(beta, TIME * NUM_AGENTS)
    else:
        steps = np.random.normal(
            0, movement_scale_factor * np.sqrt(np.pi / 2), TIME * NUM_AGENTS
        )

    angles = np.random.uniform(0, 2 * math.pi, TIME * NUM_AGENTS)

    for time_idx in range(TIME):

        for agent_idx, agent in enumerate(agents):

            index = time_idx * NUM_AGENTS + agent_idx
            # walk
            if mode == 0:
                levy_walk(agent, angles[index], steps[index])
            elif mode == 1:
                random_walk(agent, angles[index], steps[index])
            else:
                brownian_motion(agent, angles[index], steps[index])

            # Wrap agents around the screen
            agent["x"] = agent["x"] % WIDTH
            agent["y"] = agent["y"] % HEIGHT

            # Draw agents

            if agent_idx == 0:
                pass

            else:

                if (agent["x"] - agents[0]["x"]) ** 2 + (
                    agent["y"] - agents[0]["y"]
                ) ** 2 <= CIRCLE_SIZE**2:
                    if random.random() < 0.01:
                        agent["color"] = RED

    return len([agent for agent in agents if agent["color"] == RED])


if __name__ == "__main__":
    for scale_factor in np.linspace(1, 2, 10):
        num_runs = 1000
        mode_choice = 2  # 0: Levy walk, 1: Random walk, 2: Brownian motion

        NUM_AGENTS = int(100 * scale_factor)

        args = [(mode_choice, 3)] * num_runs

        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            results = pool.starmap(main, args)

        avg_result = sum(results) / num_runs
        std_dev = np.std(results)
        print(f"Average result for scale factor {scale_factor}:", avg_result)

        with open("browninan.csv", "a", encoding="utf-8") as f:
            f.write(f"{scale_factor},{avg_result},{std_dev}\n")
