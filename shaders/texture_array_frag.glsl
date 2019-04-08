#version 330
in vec3 fragmentColour;
in vec2 UV;

out vec4 outputColour;

#include shaders/global_fragment_uniforms.glsl

#include shaders/texture_fragment_uniforms.glsl
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
