echo создать эталонный message.pot
echo pybabel extract -F babel.cfg -k _l -o messages.pot .

echo добавить язык
echo pybabel init -i messages.pot -d webapp/translations -l ru creating catalog webapp/translations/ru/LC_MESSAGES/messages.po based on messages.pot
echo pybabel init -i messages.pot -d webapp/translations -l en creating catalog webapp/translations/en/LC_MESSAGES/messages.po based on messages.pot

echo компиляция в mo
echo pybabel compile -d webapp/translations compiling catalog webapp/translations/ru/LC_MESSAGES/messages.po to webapp/translations/ru/LC_MESSAGES/messages.mo
echo pybabel compile -d webapp/translations compiling catalog webapp/translations/en/LC_MESSAGES/messages.po to webapp/translations/en/LC_MESSAGES/messages.mo

echo обновление
pybabel extract -F babel.cfg -k _l -o messages.pot .
pybabel update -i messages.pot -d webapp/translations