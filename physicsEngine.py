import pybullet as p
import pybullet_data
import time
import numpy as np

# Start the physics engine in GUI mode for visualization
physicsClient = p.connect(p.GUI)

# Load basic environment
p.setGravity(0, 0, -10)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Load a plane to represent your brass plate
planeId = p.loadURDF("brassPlate.urdf")

# Optionally, adjust the visual properties of the plane
# This is more for aesthetics if you're simulating a brass plate

sand_particle_radius = 0.0015  # Half of 0.3mm in meters
for _ in range(100):  # Example: 100 particles
    # Position particles above the plate with random x, y, and a fixed height
    x = np.random.uniform(-0.5, 0.5)
    y = np.random.uniform(-0.5, 0.5)
    z = 0.1  # Height above the plate
    p.loadURDF("sphere_small.urdf", basePosition=[x, y, z])


# Example: Apply a periodic force to the plate or directly to particles
# This is a simplified approach; real vibrations would be more complex
for i in range(10000):
    # Apply a force vector that changes over time to simulate vibration
    # This is highly simplified and would need refinement for accuracy
    p.applyExternalForce(planeId, -1, [0, 0, np.sin(i * 0.1)], [0, 0, 0], p.WORLD_FRAME)
    p.stepSimulation()
    time.sleep(1./240.)  # Simulation step delay
