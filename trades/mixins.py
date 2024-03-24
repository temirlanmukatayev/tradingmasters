class OwnerMixin:
    """Check if object is created by the user."""
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
    

class OwnerEditMixin:
    """Check if the user can edit the object."""
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)