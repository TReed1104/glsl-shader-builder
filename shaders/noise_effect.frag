#version 330
out vec4 outputColour;

#include components/global_fragment_uniforms.glsl

#include components/global_fragment_functions.glsl

float noise(in vec2 st){
	// taken from examples online
	vec2 i = floor(st);
	vec2 f = fract(st);
	
	// Four corners in 2D of a tile
	float a = random(i);
	float b = random(i + vec2(1.0f, 0.0f));
	float c = random(i + vec2(0.0f, 1.0f));
	float d = random(i + vec2(1.0f, 1.0f));
	
	// Smooth Interpolation
	vec2 u = f * f * (3.0f - 2.0f * f);// Cubic Hermine Curve.
	
	return mix(a, b, u.x) + (c - a) * u.y * (1.0f - u.x) + (d - b) * u.x * u.y;
}

void main(){
	float clampedNosie = mod(noise(gl_FragCoord.xy) * (u_time), 1);
	outputColour = vec4(vec3(clampedNosie), 1.0f);
}
