#version 330
#include components/fragment_in.glsl

out vec4 outputColour;

#include components/global_uniforms.glsl

#include components/lighting_uniforms.glsl

void main() {
    // Ambient calculations
    vec3 ambient = (ambientStrength * lightingColor);

    // Calculate the fragment colour using the vertex colour and ambient lighting values
    outputColour = vec4((ambient * fragmentColour), 1.0);
}