class VkAPIError(Exception):
    def __init__(self, error_code: int = None, error_msg: str = None, error_request_params: dict = None):
        self.error_code = error_code
        self.error_msg = error_msg
        self.error_request_params = error_request_params

    def __str__(self):
        return f"{self.error_request_params}, {self.error_msg}, {self.error_code}"


class UnknownErrorHasOccurred(VkAPIError):
    pass


class TheApplicationIsDisabled(VkAPIError):
    pass


class UnknownMethodPassed(VkAPIError):
    pass


class InvalidSignature(VkAPIError):
    pass


class UserAuthorizationFailed(VkAPIError):
    pass


class TooManyRequestsPerSecond(VkAPIError):
    pass


class YouDoNotHavePermissionToPerformThisAction(VkAPIError):
    pass


class InvalidRequest(VkAPIError):
    pass


class TooManySimilarActions(VkAPIError):
    pass


class AnInternalServerErrorHasOccurred(VkAPIError):
    pass


class InTestModeTheApplicationMustBeTurnedOffOrTheUserMustBeLoggedIn(VkAPIError):
    pass


class YouNeedToEnterTheCodeFromTheImageCaptcha(VkAPIError):
    pass


class AccessIsDenied(VkAPIError):
    pass


class RequestsMustBeMadeOverHTTPSBecauseTheUserHasEnabledASettingThatRequiresWorkOverASecureConnection(VkAPIError):
    pass


class UserValidationRequired(VkAPIError):
    pass


class UserWasDeletedOrBanned(VkAPIError):
    pass


class ThisActionIsProhibitedForNonStandaloneApplications(VkAPIError):
    pass


class ThisActionIsAllowedOnlyForStandaloneAndOpenAPIApplications(VkAPIError):
    pass


class TheMethodHasBeenDisabled(VkAPIError):
    pass


class UserConfirmationRequired(VkAPIError):
    pass


class TheCommunityAccessKeyIsInvalid(VkAPIError):
    pass


class TheApplicationAccessKeyIsInvalid(VkAPIError):
    pass


class QuantityLimitPerMethodCallReached(VkAPIError):
    pass


class ProfileIsPrivate(VkAPIError):
    pass


class OneOfTheRequiredParametersWasNotPassedOrIsInvalid(VkAPIError):
    pass


class InvalidApplicationAPIID(VkAPIError):
    pass


class InvalidUserID(VkAPIError):
    pass


class InvalidTimestamp(VkAPIError):
    pass


class AlbumAccessDenied(VkAPIError):
    pass


class AudioAccessDenied(VkAPIError):
    pass


class GroupAccessDenied(VkAPIError):
    pass


class AlbumFull(VkAPIError):
    pass


class ActionDeniedYouMustEnableVoiceTranslationsInTheAppSettings(VkAPIError):
    pass


class NoRightsToPerformTheseOperationsWithTheAdvertisingAccount(VkAPIError):
    pass


class AnErrorOccurredWhileWorkingWithTheAdvertisingAccount(VkAPIError):
    pass


class SpecifiedLinkIsIncorrectCantFindSource(VkAPIError):
    pass


class AccessToPostCommentsDenied(VkAPIError):
    pass


class AccessToStatusRepliesDenied(VkAPIError):
    pass


class HyperlinksAreForbidden(VkAPIError):
    pass


class TooManyReplies(VkAPIError):
    pass


class AccessToWallsPostDenied(VkAPIError):
    pass


class AccessToWallsCommentDenied(VkAPIError):
    pass


class TooManyAdsPosts(VkAPIError):
    pass


class DonutIsDisabled(VkAPIError):
    pass


class ContentBlocked(VkAPIError):
    pass


class AccessToAddingPostDenied(VkAPIError):
    pass


class AdvertisementPostWasRecentlyAdded(VkAPIError):
    pass


class TooManyRecipients(VkAPIError):
    pass
