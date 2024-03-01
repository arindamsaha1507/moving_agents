# import pygame
import random
import math
import multiprocessing

import numpy as np

WIDTH, HEIGHT = 1000, 1000
AGENT_SIZE = 5
NUM_AGENTS = 100
CIRCLE_SIZE = 50

TIME = 3000

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


def levy_walk(agent, angle, movement_scale_factor):
    # Generate a step length from a Levy distribution (power-law distribution)

    beta = movement_scale_factor / (
        movement_scale_factor - 1
    )  # Adjust this value for different Levy distributions

    # beta = movement_scale_factor  # Adjust this value for different Levy distributions
    # beta = 1.5  # Adjust this value for different Levy distributions
    step_length = random.paretovariate(beta)

    # Update agent's position based on the new angle and step length
    agent["x"] += step_length * math.cos(angle)
    agent["y"] += step_length * math.sin(angle)


def random_walk(agent, angle, movement_scale_factor):
    step_length = movement_scale_factor

    if angle < math.pi / 2:
        agent["x"] += step_length
    elif angle < math.pi:
        agent["y"] += step_length
    elif angle < 3 * math.pi / 2:
        agent["x"] -= step_length
    else:
        agent["y"] -= step_length


def brownian_motion(agent, angle, movement_scale_factor):

    step_length = np.random.normal(0, movement_scale_factor * np.sqrt(np.pi / 2))

    angle += random.uniform(-math.pi / 2, math.pi / 2)

    agent["x"] += step_length * math.cos(angle)
    agent["y"] += step_length * math.sin(angle)


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

    for _ in range(TIME):

        for idx, agent in enumerate(agents):
            # walk
            if mode == 0:
                levy_walk(agent, random.uniform(0, 2 * math.pi), movement_scale_factor)
            elif mode == 1:
                random_walk(
                    agent, random.uniform(0, 2 * math.pi), movement_scale_factor
                )
            else:
                brownian_motion(
                    agent, random.uniform(0, 2 * math.pi), movement_scale_factor
                )

            # Wrap agents around the screen
            agent["x"] = agent["x"] % WIDTH
            agent["y"] = agent["y"] % HEIGHT

            # Draw agents

            if idx == 0:
                pass

            else:

                if (agent["x"] - agents[0]["x"]) ** 2 + (
                    agent["y"] - agents[0]["y"]
                ) ** 2 <= CIRCLE_SIZE**2:
                    if random.random() < 0.01:
                        agent["color"] = RED

    return len([agent for agent in agents if agent["color"] == RED])


if __name__ == "__main__":

    for scale_factor in np.linspace(1, 2, 100):

        num_runs = 100
        mode_choice = 1  # 0: Levy walk, 1: Random walk 2: Brownian motion

        NUM_AGENTS = int(100 * scale_factor)

        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            results = [
                pool.apply(main, args=(mode_choice, 3))
                for _ in range(num_runs)
            ]
            # results = pool.map(main, [mode] * num_runs)

        avg_result = sum(results) / num_runs
        std_dev = np.std(results)
        print(f"Average result for scale factor {scale_factor}:", avg_result)
        # print("Average result:", avg_result)

        with open("scale_random.csv", "a", encoding="utf-8") as f:
            f.write(f"{scale_factor},{avg_result},{std_dev}\n")
