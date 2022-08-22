from color import Color
from point import Point
from vector import Vector
from sphere import Sphere
from light import Light
from material import Material, CheckeredMaterial

WIDTH = 960
HEIGHT = 540
RENDERED_IMG = "2balls.ppm"
CAMERA = Vector(0, -0.35, -1)
OBJECTS = [
	# Ground Plane
	Sphere(
		Point(0, 10000.5, 1), 
		10000.0, 
		CheckeredMaterial(
			color1 = Color.from_hex("#111111"), 
			color2 = Color.from_hex("#888888"),
			ambient = 0.2, 
			reflection = 0.2
		)
	),
	# Cyan ball
	Sphere(Point(0.75, -0.1, 1), 0.6, Material(Color.from_hex("#00FFFF"))), 
	# Pink ball
	Sphere(Point(-0.75, -0.1, 2.25), 0.6, Material(Color.from_hex("#803980")))
]
LIGHTS = [
	Light(Point(1.5, -0.5, -10.0), Color.from_hex("#FFFFFF")),
	Light(Point(-0.5, -10.5, 0.0), Color.from_hex("#E6E6E6"))
]