# TODO List
- [ ] Сделать рефакторинг: в place_entities_in_init_positions(), в set_entity_on_map - в class_name(coordinate)
необходимо передавать, в том числе, w, h и color (если entity: Entity). Сейчас - type: ignore;
- [x] Можно ли передавать w и h = TILESIZE - в Creature, а лучше в Entity - как значение по умолчанию, и не передавать их при инициализации объектов?
