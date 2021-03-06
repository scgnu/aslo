from . import web
from flask import render_template, abort
from aslo.persistence.activity import Activity
from aslo.service import activity as activity_service


@web.route('/')
def index():
    activities = Activity.get_all()
    return render_template('index.html', activities=activities)


@web.route('/<bundle_id>/<activity_version>', strict_slashes=False)
def activity_detail(bundle_id, activity_version):
        activity_version = float(activity_version)
        activity = Activity.get_by_bundle_id(bundle_id)
        if activity is None:
            abort(404)

        release = activity_service.find_release(activity, activity_version)
        if release is None:
            abort(404)
        else:
            return render_template('detail.html', activity=activity,
                                   current_release=release)
