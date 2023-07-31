import {
  defineConfig,
  presetIcons,
  presetTypography,
  presetUno,
  presetWebFonts,
  transformerVariantGroup,
} from "unocss";

const fonts = {
  sans: [
    {
      name: "Noto Sans JP",
      weights: ["400", "500"],
    },
  ],
  mono: [
    {
      name: "Noto Sans Mono",
      weights: ["400", "500"],
    },
  ],
};

export default defineConfig({
  presets: [
    presetUno(),
    presetIcons(),
    presetTypography(),
    presetWebFonts({ provider: "none", fonts }),
  ],
  transformers: [transformerVariantGroup()],
});
