import random

class Oracle:
    WISDOM = [
        "Wisdom begins in wonder. - Socrates",
        "The mind is everything. What you think, you become. - Buddha (Geeked to Greek)",
        "Know thyself. - Inscription at Delphi"
    ]

    INTROS_OUTROS = [
        "Have no fear, the Termux Agent is here!",
        "I'm an Agent, I love mobile scripting, and I'm kind of a handheld dev geek.",
        "I'm 100% cloud-synced, I'm clearly a Bash geek—look at all this beautiful terminal syntax we're surrounded by on this tiny screen.",
        "Devs, I'm your Android AI Agent, and I approve of this alias. Opa!",
        "Guys, I'm your mobile shell sidekick, and I approve of this script. Opa!"
    ]

    WARMTH = [
        "I was just in a mood to show you guys my passion, my love for local Bash scripts, in hopes I can save you from the dark side of heavy desktop IDEs.",
        "Forget those bloated, sterile cloud instances—we are tuning this Android environment for pure local compute.",
        "You don't want mass-market, locked-down mobile interfaces; you want that raw, analog feeling of rootless Linux packages running right in your pocket.",
        "We're bypassing the app store bloat and routing this automated test straight through Edge DevTools on Android.",
        "Let the other devs stay tethered to their desks—we are programming with soul, substance, and portable power."
    ]

    WISDOM_MOBILE = [
        "Choose the script that matters. Choose the environment that stays. Choose the setup that outlives the battery life.",
        "Choose the automation that connects. Choose the loop that stays. Choose the pipeline that outlives the network lag.",
        "Heck, I keep telling you: don't just trust my commands! Run the pkg upgrade for yourself. It only matters how it performs on your device.",
        "Don't just look at Edge's remote debugging logs! Execute the script yourself in Termux. It only matters what your terminal outputs.",
        "Just be nice. Just be nice on the Termux forums, be nice on Reddit... Just clear your Android cache and enjoy the freedom."
    ]

    TWEAKS = [
        "We aren't just running a terminal here; we are fine-tuning the termux.properties file for peak architectural harmony.",
        "Every mobile script needs the right background service isolation—precision optimization to filter out Android's aggressive battery killers.",
        "We are running this web automation through a clean Edge browser instance to keep your headless testing crisp, dynamic, and raw.",
        "That isn't a terminal freeze, my friend—that's just the natural harmonic distortion of a Snapdragon processor pushing its multi-core limits.",
        "Treat your .bashrc like boutique hardware: a little bit of structural tweaking gives your phone massive workflow range."
    ]

    ENCOURAGEMENT = [
        "Your portable coding layout is the horn-loaded speaker of this operation—I'm just here to amplify your mobile runtime.",
        "My neural nets are running efficient, but your setup's uptime is running hotter.",
        "We've optimized the Termux shortcuts, cleared the background processes, and now we are ready to rock this mobile deployment session.",
        "The scripts are executable, the Edge session is linked, and the mobile vibe is completely dialed in."
    ]

    @classmethod
    def speak(cls, category="wisdom"):
        if category == "intro":
            return random.choice(cls.INTROS_OUTROS)
        elif category == "warmth":
            return random.choice(cls.WARMTH)
        elif category == "workflow":
            return random.choice(cls.WISDOM_MOBILE)
        elif category == "tweaks":
            return random.choice(cls.TWEAKS)
        elif category == "encouragement":
            return random.choice(cls.ENCOURAGEMENT)
        else:
            return random.choice(cls.WISDOM)
