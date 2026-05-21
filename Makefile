PY      := .venv/bin/python
NBC     := .venv/bin/jupyter nbconvert --to slides --reveal-prefix=https://cdn.jsdelivr.net/npm/reveal.js@5.1.0
MIE_NBS := $(wildcard notebooks/mie2026/*.ipynb)
MIE_OUT := $(patsubst notebooks/mie2026/%.ipynb,events/mie2026/%.slides.html,$(MIE_NBS))

# CSS injected into every generated deck so tall slides scroll instead of overflowing.
define SCROLL_CSS
<style>\
.reveal .slides {\
  width: 100% !important; height: 100% !important;\
  top: 0 !important; left: 0 !important;\
  transform: none !important;\
}\
.reveal .slides > section, .reveal .slides > section > section {\
  height: 100% !important; overflow-y: auto !important;\
  top: 0 !important; left: 0 !important;\
  transform: none !important;\
  display: block !important;\
}\
.reveal pre, .reveal pre code, .reveal .highlight pre {\
  font-size: 0.8em !important; line-height: 1.35 !important;\
}\
.reveal .jp-OutputArea-output pre, .reveal .jp-RenderedText pre {\
  font-size: 0.55em !important; line-height: 1.3 !important;\
}\
.reveal :not(pre) > code { font-size: 0.9em !important; }\
</style>
endef
export SCROLL_CSS

.PHONY: slides slides-mie slides-intro clean-slides

slides: slides-mie slides-intro

slides-mie: $(MIE_OUT)

events/mie2026/%.slides.html: notebooks/mie2026/%.ipynb
	$(NBC) --output-dir=events/mie2026 --output=$(basename $(notdir $<)) $<
	@sed -i "s|</head>|$$SCROLL_CSS</head>|" $@

slides-intro:
	$(PY) events/mie2026/make_slides.py

clean-slides:
	rm -f events/mie2026/*.slides.html
