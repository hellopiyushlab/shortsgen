# not required anymore, run app.py for flask server

from modules.summarizer import summarize_article
from modules.text_to_speech import text_to_speech_files
from modules.movie_maker import create_video

# hard coded article for now
article = '''That's where Shōgun comes in. FX's adaptation of James Clavell's bestselling 1975 historical fiction novel seemed like a losing prospect to many. Based on an arguably outdated IP that was best known by a generation or two before the much sought out 18-25 demographic that TV studios are known to chase, the show had mostly gone under the radar until its release. Still, as soon as the first trailer was released, the Game of Thrones comparisons began — despite Shōgun not being a fantasy. But since its very first episode, the show has transcended those comparisons and crafted something truly unique that has shown just what prestige TV can really achieve: great storytelling that captures the imagination and sets watercooler talk alight.

Set in 1600, the series follows the often brutal machinations and interpersonal politics of the leaders of Japan in the wake of the death of Nakamura Hidetoshi (Yukijiro Hotaru), their former Taikō (retired regent) who left a son too young to take on the role from him. To build a political stalemate on his deathbed, Taikō crafted a Council of Regents — made of men who would attempt to take over — to rule until his son came of age. We join the fray a year after that shocking loss when an Englishman named John Blackthorne (Cosmo Jarvis) washes up on shore along with his ship the Erasmus and the leftovers of his starving and desperately ill crew. It's an expansive setup with threads that spool across the globe, as religious powers and monarchs battle to keep their hold on what they see as a new prosperous colony. 


At the center of the conflict is legendary Japanese actor Hiroyuki Sanada as Lord Yoshi Toranaga, a noble man who turned down the chance to be sole regent and a year later is surely regretting that choice as his fellow council members are planning his impeachment and death. His charge, Mariko (Anna Sawai), is in servitude to Toranaga after the death of her father. Then there's the charming and reckless Yabushige (Tadanobu Asano). Of course, John's arrival throws everything into disarray with each of the regent council realizing he might be able to sway the war in their favor. All of that politics and the vibrant historical setting do immediately bring Game of Thrones to mind, but unlike HBO's smash hit, this is no fantasy. Instead, this is a true historical drama that transports viewers to ancient Japan thanks to incredible craft and production design. And that's not the only way in which Shōgun transcends the series it's so often compared to.

'''
#get a list of sentences of summary
summarized_article, summarized_article_list_of_sentences = summarize_article(article)
print(summarized_article_list_of_sentences)

# text to speech
saved_audio_files = text_to_speech_files(summarized_article_list_of_sentences)

print("Audio files saved at the following locations:")
for file_path in saved_audio_files:
    print(file_path)

# movie generation
create_video(summarized_article_list_of_sentences)