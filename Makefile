.PHONY: a-events g-events profile-inst profile-ta

profile-ta:
	python3 scripts/make-profile.py data/profile-ta docs/assets/profile-ta docs/static/data/profile_ta.json

profile-inst:
	python3 scripts/make-profile.py data/profile-inst docs/assets/profile-inst docs/static/data/profile_inst.json

g-events:
	python3 scripts/make-events.py --mode g \
		--start_date 2025-02-17  \
		--end_date 2025-06-30  \
		--location "主B-204" \
		--weeks 2 4 \
		--json docs/static/data/events.json

TITLE ?=
START_TIME ?=
END_TIME ?=
TEACHER ?=
LOCATION ?=
THEME ?=
a-events:
	python3 scripts/make-events.py --mode a --title $(TITLE) \
		--start_time $(START_TIME) \
		--end_time $(END_TIME) \
	    --teacher $(TEACHER) \
		--location $(LOCATION) \
		--theme $(THEME) \
		--json docs/static/data/events.json

