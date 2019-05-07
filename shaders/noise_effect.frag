#version 330
#include components/fragment_in.glsl

#include components/fragment_out.glsl

#include components/global_uniforms.glsl

#include components/global_functions.glsl

void main(){
	float clampedNosie = mod(noise(gl_FragCoord.xy) * (u_time), 1);
	outputColour = vec4(vec3(clampedNosie), 1.0f);
}
