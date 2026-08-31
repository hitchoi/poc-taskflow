from taskflow import TaskFlow


def test_add_and_count():
    tf = TaskFlow()
    tf.add("문서 작성", priority=2)
    tf.add("코드 리뷰", priority=5)
    assert len(tf.list(include_done=True)) == 2


def test_complete_marks_done():
    tf = TaskFlow()
    tf.add("배포")
    assert tf.complete("배포") is True
    assert tf.complete("없는작업") is False
