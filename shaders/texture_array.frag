#version 330
#include components/fragment_in.glsl

out vec4 outputColour;

#include components/global_uniforms.glsl

#include components/texture_uniforms.glsl
uniform int u_textureArrayLayer;

void main() {
	if (u_hasTexture) {
		outputColour = texture(u_textureSampler, vec3(UV, u_textureArrayLayer));
	}
	else {
		// Texturing has not been setup, use the colour buffer.
		outputColour = vec4(fragmentColour, 1.0f);
	}
}
