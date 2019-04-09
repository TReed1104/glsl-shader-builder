#version 330
out vec4 outputColour;

#include components/global_uniforms.glsl

#include components/global_functions.glsl

void main(){
	float clampedNosie = mod(noise(gl_FragCoord.xy) * (u_time), 1);
	outputColour = vec4(vec3(clampedNosie), 1.0f);
}
