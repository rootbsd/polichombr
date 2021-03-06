"""
    This file is part of Polichombr.

    (c) 2016 ANSSI-FR


    Description:
        Forms used in the web interface.
"""

from flask_wtf import Form
from flask_security import RegisterForm
from wtforms import StringField, FileField, SelectField
from wtforms import SubmitField, TextAreaField, BooleanField
from wtforms import PasswordField, HiddenField
from wtforms import IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, InputRequired
from poli.models.family import DetectionType
from poli.models.models import TLPLevel

"""
    USER forms.
"""

class ChgThemeForm(Form):
    """
    Change user's theme.
    """
    choices = [
        ("dark", 'dark'),
        ("std", 'regular')
    ]
    newtheme = SelectField('Theme', choices=choices,
                           coerce=str, validators=[DataRequired()])
    changetheme = SubmitField(u'Submit')


class ChgNickForm(Form):
    """
    Change user's nickname (login).
    """
    newnick = StringField("New nick", validators=[DataRequired()])
    changenick = SubmitField(u'Submit')


class ChgNameForm(Form):
    """
    Change user's full name.
    """
    newname = StringField("New name", validators=[DataRequired()])
    changename = SubmitField(u'Submit')


class ChgPassForm(Form):
    """
    Change user's password.
    """
    oldpass = PasswordField("Old password", validators=[DataRequired()])
    password = PasswordField(
        'New password', validators=[
            Length(min=6),
            DataRequired(),
            EqualTo('rpt_pass',
                    message='Confirmation must match')])
    rpt_pass = PasswordField('Confirm password')
    changepass = SubmitField(u'Submit')


class LoginForm(Form):
    """
    User login.
    """
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[Length(min=6)])
    userlogin = SubmitField(u'Submit')


class UserRegistrationForm(Form):
    """
    User registration.
    """
    username = StringField('Username', validators=[DataRequired()])
    completename = StringField('Complete name', validators=[DataRequired()])
    password = PasswordField(
        'password', validators=[
            Length(min=6),
            DataRequired(),
            EqualTo('rpt_pass',
                    message='Confirmation must match')])
    rpt_pass = PasswordField('Confirm password')
    userregister = SubmitField(u'Submit')


"""

    SETTINGS forms.

"""


class CreateCheckListForm(Form):
    """
    Create new checklist item.
    """
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Title", validators=[DataRequired()])
    changepoke = SubmitField(u'Submit')


"""

    YARA forms.

"""


class YaraForm(Form):
    """
    Create yara.
    """
    yara_name = StringField('yaraname', validators=[DataRequired()])
    choices = [
        (TLPLevel.TLPWHITE, 'TLP White'),
        (TLPLevel.TLPGREEN, 'TLP Green'),
        (TLPLevel.TLPAMBER, 'TLP Amber'),
        (TLPLevel.TLPRED, 'TLP Red'),
        (TLPLevel.TLPBLACK, 'TLP Black'),
    ]
    yara_tlp = SelectField('Sensibility', choices=choices,
                           coerce=int, validators=[DataRequired()])
    yara_raw = TextAreaField('Yaradata', validators=[DataRequired()])
    createyara = SubmitField(u'Submit')


"""

    FAMILIES forms.

"""


class FamilyForm(Form):
    """
    Create family.
    """
    familyname = StringField('familyname', validators=[DataRequired()])
    createfamily = SubmitField(u'Submit')


class AddSubFamilyForm(Form):
    """
    Create sub-family.
    """
    familyname = StringField('Sub-family name', validators=[DataRequired()])
    subfamily = SubmitField(u'Create')


class UploadFamilyFileForm(Form):
    """
    Add family file.
    """
    file = FileField('File', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    choices = [
        (TLPLevel.TLPWHITE, 'TLP White'),
        (TLPLevel.TLPGREEN, 'TLP Green'),
        (TLPLevel.TLPAMBER, 'TLP Amber'),
        (TLPLevel.TLPRED, 'TLP Red'),
        (TLPLevel.TLPBLACK, 'TLP Black'),
    ]
    level = SelectField(u'Sensibility', choices=choices,
                        coerce=int, validators=[DataRequired()])
    uploadfile = SubmitField(u'Submit')


class CreateDetectionItemForm(Form):
    """
    Add detection item.
    """
    name = StringField(u'Name', validators=[DataRequired()])
    abstract = TextAreaField(u'Abstract', validators=[DataRequired()])
    choices = [
        (DetectionType.CUSTOM, 'Custom'),
        (DetectionType.OPENIOC, 'OpenIOC'),
        (DetectionType.SNORT, 'Snort')
    ]
    item_type = SelectField(
        u'Type',
        choices=choices,
        coerce=int,
        validators=[
            DataRequired()])
    choices = [
        (TLPLevel.TLPWHITE, 'TLP White'),
        (TLPLevel.TLPGREEN, 'TLP Green'),
        (TLPLevel.TLPAMBER, 'TLP Amber'),
        (TLPLevel.TLPRED, 'TLP Red'),
        (TLPLevel.TLPBLACK, 'TLP Black'),
    ]
    tlp_level = SelectField(
        u'Sensibility',
        choices=choices,
        coerce=int,
        validators=[
            DataRequired()])
    createitem = SubmitField(u'Create')


class ChangeTLPForm(Form):
    """
    Change TLP level.
    """
    choices = [
        (TLPLevel.TLPWHITE, 'TLP White'),
        (TLPLevel.TLPGREEN, 'TLP Green'),
        (TLPLevel.TLPAMBER, 'TLP Amber'),
        (TLPLevel.TLPRED, 'TLP Red'),
        (TLPLevel.TLPBLACK, 'TLP Black'),
    ]
    item_id = HiddenField(u'item_id')
    level = SelectField(u'', choices=choices,
                        coerce=int, validators=[DataRequired()])
    changetlp = SubmitField(u'Change TLP level')


class ChangeStatusForm(Form):
    """
    Change analysis status.
    """
    choices = [
        (3, 'Not started'),
        (2, 'Currently analyzed'),
        (1, 'Finished'),
    ]
    newstatus = SelectField(
        u'Status',
        choices=choices,
        coerce=int,
        validators=[
            DataRequired()])
    changestatus = SubmitField(u'Change status')


class AddYaraToFamilyForm(Form):
    """
    Add yara rule.
    """
    yaraid = SelectField(
        u'Associated yara',
        coerce=int,
        validators=[
            DataRequired()])
    addyarafam = SubmitField(u'Submit')


class RenameForm(Form):
    """
    Rename.
    """
    newname = StringField('Name', validators=[DataRequired()])
    item_id = HiddenField(u'item_id')
    rename = SubmitField(u'Rename')


class FamilyAbstractForm(Form):
    """
    Edit abstract.
    """
    abstract = TextAreaField(
        'Family abstract',
        default="Here goes the family informations",
        validators=[
            DataRequired()])
    familyabstract = SubmitField(u'Submit')


class ExportFamilyForm(Form):
    """
    Export family data.
    """
    choices = [
        (TLPLevel.TLPWHITE, 'TLP White'),
        (TLPLevel.TLPGREEN, 'TLP Green'),
        (TLPLevel.TLPAMBER, 'TLP Amber'),
        (TLPLevel.TLPRED, 'TLP Red')
    ]
    level = SelectField(u'Maximum sensibility', choices=choices,
                        coerce=int, validators=[DataRequired()])
    choices = [
        (1, "Yara rules (RULESET)"),
        (2, "Samples auto-generated indicators (OPENIOC)"),
        (3, "Custom open-ioc detection items (OPENIOC)"),
        (4, "Custom Snort detection items (SNORT)"),
        (5, "Custom generic detection items (TXT)"),
        (6, "Samples (TARGZ)")
    ]
    datatype = SelectField(u'Data type', choices=choices,
                           coerce=int, validators=[DataRequired()])
    exportfam = SubmitField('Submit')


"""

    SAMPLES forms.

"""


class UploadSampleForm(Form):
    """
    Upload sample.
    """
    file = FileField('Sample File', validators=[DataRequired()])
    choices = [
        (TLPLevel.TLPWHITE, 'TLP White'),
        (TLPLevel.TLPGREEN, 'TLP Green'),
        (TLPLevel.TLPAMBER, 'TLP Amber'),
        (TLPLevel.TLPRED, 'TLP Red'),
        (TLPLevel.TLPBLACK, 'TLP Black'),
    ]
    level = SelectField(u'Sensibility', choices=choices,
                        coerce=int, validators=[DataRequired()])
    family = SelectField(u'Associated Family', coerce=int)
    uploadsample = SubmitField(u'Submit')


class AddSampleToFamilyForm(Form):
    """
    Add sample to family.
    """
    parentfamily = SelectField(
        u'Associated family',
        coerce=int,
        validators=[
            DataRequired()])
    addsample = SubmitField(u'Submit')


class SampleAbstractForm(Form):
    """
    Edit abstract.
    """
    abstract = TextAreaField(
        'Sample abstract',
        default="My beautiful sample! ",
        validators=[DataRequired()])
    sampleabstract = SubmitField(u'Submit')


class CompareMachocForm(Form):
    """
    Compare to other samples.
    """
    percent = IntegerField(u'Minimal percent match',
                           validators=[DataRequired()])
    compare = SubmitField(u'Compare!')


class ExportMachexForm(Form):
    """
    Export MACHEX data.
    """
    machocfull = BooleanField(u'Machoc hash')
    fmachoc = BooleanField(u'Functions: machoc hashes')
    fnames = BooleanField(u'Functions: names')
    analysis_data = BooleanField(u'Analysis data')
    abstracts = BooleanField(u'Abstract')
    metadata = BooleanField(u'File metadata (PE, ELF...)')
    estrings = BooleanField(u'Strings')
    sampleid = HiddenField(
        u'sampleid',
        default="1",
        validators=[
            InputRequired()])
    export = SubmitField(u'Submit')


class ImportForm(Form):
    """
    Import MACHEX data.
    """
    file = FileField('MACHEX File', validators=[DataRequired()])
    choices = [
        (TLPLevel.TLPWHITE, 'TLP White'),
        (TLPLevel.TLPGREEN, 'TLP Green'),
        (TLPLevel.TLPAMBER, 'TLP Amber'),
        (TLPLevel.TLPRED, 'TLP Red'),
        (TLPLevel.TLPBLACK, 'TLP Black'),
    ]
    level = SelectField(u'Sensibility', choices=choices,
                        coerce=int, validators=[DataRequired()])
    importform = SubmitField(u'Submit')


"""

    SEARCH forms.

"""


class FullTextSearchForm(Form):
    """
    Full-text search.
    """
    fneedle = StringField("Search", validators=[DataRequired()])
    search = SubmitField(u'Submit')


class MachocHashSearchForm(Form):
    """
    Full machoc hash search.
    """
    percent = IntegerField("Minimum hit level")
    mneedle = StringField("Search", validators=[DataRequired()])
    search = SubmitField(u'Submit')


class HashSearchForm(Form):
    """
    Hash search.
    """
    hneedle = StringField("Search", validators=[DataRequired()])
    search = SubmitField(u'Submit')
