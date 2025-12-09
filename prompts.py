from typing import Dict, Any, List

# Internal library of block types, modes, and exercises.
# You can expand this as much as you like.
_PROMPT_LIBRARY: Dict[str, Dict[str, Any]] = {
    "perfectionism": {
        "label": "Perfectionism / fear of not being good enough",
        "prompts": {
            "quick": {
                "title": "Lower the stakes for one page",
                "description": (
                    "Perfectionism usually appears when the work feels too important "
                    "to be messy. This exercise deliberately shrinks the stakes so "
                    "you can move again."
                ),
                "exercises": [
                    {
                        "type": "freewrite",
                        "duration_minutes": 5,
                        "text": (
                            "Set a timer for 5 minutes. Rewrite your current scene as if "
                            "it were a chaotic fanfic version: exaggerate, break tone, "
                            "let it be ridiculous. The goal is not quality, only motion."
                        ),
                    }
                ],
            },
            "deep": {
                "title": "Name the critic, then ignore them",
                "description": (
                    "Perfectionism often borrows someone else’s voice. This deep-dive "
                    "makes that critic visible so you can write around them."
                ),
                "exercises": [
                    {
                        "type": "reflection",
                        "text": (
                            "On a separate page, answer: When I hesitate to write, "
                            "whose imagined opinion am I afraid of? A teacher, a parent, "
                            "a future reader, a version of myself?"
                        ),
                    },
                    {
                        "type": "reflection",
                        "text": (
                            "Write 3 short bullet points about what that critic wants "
                            "from you (e.g., 'never be cringey', 'always be profound')."
                        ),
                    },
                    {
                        "type": "writing",
                        "text": (
                            "Now write 1 paragraph in your current project that would "
                            "actively disappoint that critic but delight you. This can "
                            "be messy, vulnerable, or silly."
                        ),
                    },
                ],
            },
            "timed": {
                "title": "The 10-minute imperfect sprint",
                "description": (
                    "You commit to speed instead of polish. The only failure is not "
                    "moving your fingers."
                ),
                "exercises": [
                    {
                        "type": "setup",
                        "duration_minutes": 2,
                        "text": (
                            "Decide on: (1) character, (2) location, (3) small desire. "
                            "Example: 'Jamilla, kitchen, wants to hide the letter.'"
                        ),
                    },
                    {
                        "type": "timed",
                        "duration_minutes": 10,
                        "text": (
                            "Set a 10-minute timer. Write the scene without editing "
                            "or backspacing, even if you hate every line. If you get "
                            "stuck, write 'and then' and move one beat forward."
                        ),
                    },
                ],
            },
        },
    },
    "plot": {
        "label": "Plot problems / not knowing what happens next",
        "prompts": {
            "quick": {
                "title": "Three doors out of this scene",
                "description": (
                    "When plot feels stuck, you do not need the perfect next move. "
                    "You only need options."
                ),
                "exercises": [
                    {
                        "type": "brainstorm",
                        "text": (
                            "Write 3 different ways this scene could end in the next "
                            "2 pages. One should be predictable, one chaotic, one subtle. "
                            "Pick the one that feels most alive, not the one that feels 'smart'."
                        ),
                    }
                ],
            },
            "deep": {
                "title": "Return to the core question",
                "description": (
                    "Plots stall when they drift away from the real question of the story."
                ),
                "exercises": [
                    {
                        "type": "reflection",
                        "text": (
                            "In one sentence, answer: What is this story trying to figure out "
                            "about people or the world? (Example: 'Can loyalty survive ambition?')."
                        ),
                    },
                    {
                        "type": "reflection",
                        "text": (
                            "Now ask: How could the next scene force your main character to "
                            "answer that question badly? Outline 2 possibilities."
                        ),
                    },
                    {
                        "type": "writing",
                        "text": (
                            "Choose one possibility and write a rough half-page scene where "
                            "your character makes a choice you know they will regret later."
                        ),
                    },
                ],
            },
            "timed": {
                "title": "20 beats in 10 minutes",
                "description": (
                    "Instead of writing prose, you sketch the skeleton of several future scenes."
                ),
                "exercises": [
                    {
                        "type": "timed",
                        "duration_minutes": 10,
                        "text": (
                            "Set a 10-minute timer. Write a numbered list of 20 tiny beats "
                            "that could happen next in the story. Each beat should be no more "
                            "than one sentence. Do not evaluate, just list."
                        ),
                    },
                ],
            },
        },
    },
    "character": {
        "label": "Character issues / flat or confusing characters",
        "prompts": {
            "quick": {
                "title": "Give them a secret and a contradiction",
                "description": (
                    "Characters come alive when they want something in public and something "
                    "else in private."
                ),
                "exercises": [
                    {
                        "type": "brainstorm",
                        "text": (
                            "Pick one character. Write: (1) the thing they want people to "
                            "believe about them, and (2) the truth they never say out loud."
                        ),
                    },
                    {
                        "type": "writing",
                        "text": (
                            "Write 1 paragraph of your character lying about who they are. "
                            "Let one sentence almost reveal the truth but swerve away."
                        ),
                    },
                ],
            },
            "deep": {
                "title": "History, not personality traits",
                "description": (
                    "Instead of describing your character, you will write the moments that built them."
                ),
                "exercises": [
                    {
                        "type": "reflection",
                        "text": (
                            "List 3 specific memories that shaped this character’s worldview. "
                            "They should involve concrete scenes, not abstract labels."
                        ),
                    },
                    {
                        "type": "writing",
                        "text": (
                            "Choose one memory and write it as a short scene from the character’s "
                            "point of view, even if it never appears in the final story."
                        ),
                    },
                ],
            },
            "timed": {
                "title": "Voice sprint monologue",
                "description": (
                    "You will discover the character’s voice by letting them rant."
                ),
                "exercises": [
                    {
                        "type": "timed",
                        "duration_minutes": 7,
                        "text": (
                            "Set a 7-minute timer. In first person, let your character rant "
                            "about something trivial (line at the coffee shop, a bad movie, "
                            "their neighbor). Do not stop to edit."
                        ),
                    }
                ],
            },
        },
    },
    "burnout": {
        "label": "Burnout / exhaustion",
        "prompts": {
            "quick": {
                "title": "Make the task comically small",
                "description": (
                    "Burnout often needs a smaller promise, not more discipline."
                ),
                "exercises": [
                    {
                        "type": "writing",
                        "text": (
                            "Write just 3 sentences in your current project. They do not "
                            "need to be good or connected. When you are done, you are allowed "
                            "to stop for the day."
                        ),
                    }
                ],
            },
            "deep": {
                "title": "Check what writing is carrying",
                "description": (
                    "Sometimes the project is secretly carrying expectations about your value."
                ),
                "exercises": [
                    {
                        "type": "reflection",
                        "text": (
                            "Freewrite for 5–10 minutes on: 'If this project never got finished, "
                            "what story would I tell about myself?'"
                        ),
                    },
                    {
                        "type": "reflection",
                        "text": (
                            "Underline any sentences that sound like punishment rather than observation. "
                            "Ask: Are these actually true, or are they a voice I learned from somewhere?"
                        ),
                    },
                ],
            },
            "timed": {
                "title": "Cozy scene only",
                "description": (
                    "This is a no-angst, low-stakes scene to remind your brain that writing "
                    "can feel gentle."
                ),
                "exercises": [
                    {
                        "type": "timed",
                        "duration_minutes": 10,
                        "text": (
                            "Set a 10-minute timer. Write a scene in your world where nobody "
                            "argues, nobody dies, and something small but kind happens."
                        ),
                    }
                ],
            },
        },
    },
    "fear_of_judgment": {
        "label": "Fear of judgment / sharing your work",
        "prompts": {
            "quick": {
                "title": "Write for one specific person",
                "description": (
                    "Instead of 'the internet', you write for one reader who is already on your side."
                ),
                "exercises": [
                    {
                        "type": "writing",
                        "text": (
                            "Think of one person who would root for your writing. Write a short "
                            "note at the top of the page addressing them: what do you hope they "
                            "feel when they read this? Then write 1 paragraph as if only they "
                            "will ever see it."
                        ),
                    }
                ],
            },
            "deep": {
                "title": "Separate craft from performance",
                "description": (
                    "This exercise separates the private practice of writing from the public act of sharing."
                ),
                "exercises": [
                    {
                        "type": "reflection",
                        "text": (
                            "List what is fully under your control (time spent, curiosity, revision) "
                            "and what is not (other people’s reactions, algorithm, timing)."
                        ),
                    },
                    {
                        "type": "writing",
                        "text": (
                            "Write a short paragraph you promise yourself you will never share. "
                            "Make it honest and messy. This is proof that some writing can exist "
                            "just for you."
                        ),
                    },
                ],
            },
            "timed": {
                "title": "Ugly draft challenge",
                "description": (
                    "You will intentionally make the draft bad to prove that you can survive it."
                ),
                "exercises": [
                    {
                        "type": "timed",
                        "duration_minutes": 8,
                        "text": (
                            "Set an 8-minute timer. Write the most over-the-top, melodramatic version "
                            "of your current scene. Extra clichés are rewarded. When the timer ends, "
                            "delete the last sentence. Notice that you are still here."
                        ),
                    }
                ],
            },
        },
    },
    "general": {
        "label": "I just feel stuck / general block",
        "prompts": {
            "quick": {
                "title": "Change one axis of the scene",
                "description": (
                    "If you are stuck, you often just need a small shift in angle."
                ),
                "exercises": [
                    {
                        "type": "brainstorm",
                        "text": (
                            "Take the scene you are stuck on. Change exactly one thing: the weather, "
                            "the time of day, the point of view, or the emotional tone. Write 5 new lines "
                            "of the scene with that change applied."
                        ),
                    }
                ],
            },
            "deep": {
                "title": "Reconnect to why this story matters to you",
                "description": (
                    "Blocks feel heavier when we forget the original spark."
                ),
                "exercises": [
                    {
                        "type": "reflection",
                        "text": (
                            "Answer in a paragraph: When did you first get the idea for this project, "
                            "and what emotion made you say 'I have to write this'?"
                        ),
                    },
                    {
                        "type": "writing",
                        "text": (
                            "Write a short scene that amplifies that original emotion, even if it is "
                            "not part of the official plot."
                        ),
                    },
                ],
            },
            "timed": {
                "title": "Menu of tiny moves",
                "description": (
                    "Instead of one big next step, you pick from a menu of tiny actions."
                ),
                "exercises": [
                    {
                        "type": "timed",
                        "duration_minutes": 10,
                        "text": (
                            "Set a 10-minute timer. In that time, complete as many of these as you can: "
                            "(1) rename one character, (2) add one sensory detail to a scene, "
                            "(3) write one line of sharp dialogue, (4) jot one question you still have "
                            "about the story."
                        ),
                    }
                ],
            },
        },
    },
}

# Supported modes and labels, so the frontend can show them nicely.
_MODE_LABELS: Dict[str, str] = {
    "quick": "Quick spark",
    "deep": "Deep dive",
    "timed": "Timed challenge",
}


def get_block_types() -> List[Dict[str, str]]:
    """Return block types as a list of {key, label} for the UI."""
    return [
        {"key": key, "label": value["label"]}
        for key, value in _PROMPT_LIBRARY.items()
    ]


def get_modes() -> List[Dict[str, str]]:
    """Return supported modes as a list of {key, label} for the UI."""
    return [
        {"key": key, "label": label} for key, label in _MODE_LABELS.items()
    ]


def generate_spark(block_type: str, mode: str) -> Dict[str, Any]:
    """
    Generate a spark for the given block type and mode.

    Raises ValueError for unknown modes.
    Unknown or empty block types fall back to 'general'.
    """
    normalized_block = (block_type or "").strip().lower()
    normalized_mode = (mode or "").strip().lower()

    if normalized_block not in _PROMPT_LIBRARY:
        normalized_block = "general"

    if normalized_mode not in _MODE_LABELS:
        raise ValueError(f"Unknown mode: {mode!r}. Valid modes: {list(_MODE_LABELS)}")

    block_info = _PROMPT_LIBRARY[normalized_block]
    prompts_for_block = block_info["prompts"]

    if normalized_mode not in prompts_for_block:
        # If a specific block does not define that mode, fall back to quick
        normalized_mode = "quick"

    prompt_data = prompts_for_block[normalized_mode]

    # Build a response dictionary
    return {
        "block_key": normalized_block,
        "block_label": block_info["label"],
        "mode_key": normalized_mode,
        "mode_label": _MODE_LABELS[normalized_mode],
        "title": prompt_data["title"],
        "description": prompt_data["description"],
        "exercises": prompt_data["exercises"],
    }
