from modeltranslation.translator import translator, TranslationOptions
from .models import Faculty, Professor, Student, Course

class FacultyTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

class ProfessorTranslationOptions(TranslationOptions):
    fields = ('title', 'bio',)

class StudentTranslationOptions(TranslationOptions):
    fields = ()

class CourseTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

translator.register(Faculty, FacultyTranslationOptions)
translator.register(Professor, ProfessorTranslationOptions)
translator.register(Student, StudentTranslationOptions)
translator.register(Course, CourseTranslationOptions)
