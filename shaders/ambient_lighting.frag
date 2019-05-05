#version 330
#include components/fragment_in.glsl

out vec4 outputColour;

#include components/global_uniforms.glsl

// Lighting
uniform vec3 lightingColor;
uniform float ambientStrength;  // How strong is the ambient lighting?

void main() {
    vec3 ambient = (ambientStrength * lightingColor) * fragmentColour;
    outputColour = vec4(ambient, 1.0);
}